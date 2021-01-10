import pelican

try:
    import markdown
except ImportError:
    markdown = None

try:
    import yaml
except ImportError:
    yaml = None


class MarkdownYAMLReader(pelican.readers.MarkdownReader):
    """Reader for Markdown files with YAML metadata"""

    enabled = markdown is not None and yaml is not None
    file_extensions = ["md", "markdown", "mkd", "mdown"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        extension_configs = self.settings["MARKDOWN"]["extension_configs"]
        extension_config = extension_configs.setdefault(
            "full_yaml_metadata",
            {},
        )
        if "yaml_loader" not in extension_config:
            extension_config.setdefault("yaml_loader", yaml.BaseLoader)
        extensions = self.settings["MARKDOWN"]["extensions"]
        if "full_yaml_metadata" not in extensions:
            extensions.append("full_yaml_metadata")
        if "markdown.extensions.meta" in extensions:
            extensions.remove("markdown.extensions.meta")

    def _parse_metadata(self, meta):
        self._md.preprocessors.deregister("full_yaml_metadata")

        formatted_fields = self.settings["FORMATTED_FIELDS"]

        output = {}
        for name, value in meta.items():
            name = name.lower()
            if name in formatted_fields:
                # reset the markdown instance to clear any state
                self._md.reset()
                formatted = self._md.convert(value)
                output[name] = self.process_metadata(name, formatted)
            else:
                output[name] = self.process_metadata(name, value)

        return output

    def read(self, source_path):
        """Parse content and metadata of Markdown files with YAML metadata"""

        self._source_path = source_path
        self._md = markdown.Markdown(**self.settings["MARKDOWN"])
        with pelican.utils.pelican_open(source_path) as text:
            content = self._md.convert(text)

        if hasattr(self._md, "Meta") and self._md.Meta is not None:
            metadata = self._parse_metadata(self._md.Meta)
        else:
            metadata = {}

        return content, metadata


def add_reader(readers):
    for k in MarkdownYAMLReader.file_extensions:
        readers.reader_classes[k] = MarkdownYAMLReader


def register():
    pelican.signals.readers_init.connect(add_reader)
