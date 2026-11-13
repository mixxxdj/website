title: "How Mixxx fits into an Online Radio workflow"
authors: Tiphaine Chevé
tags: broadcasting radioking
status: draft
comments: yes

For an online radio broadcaster, Mixxx is often where the live show begins. You load your tracks, connect a microphone, mix your audio and click **Start Broadcasting** .

But what happens after that?

The audio produced by Mixxx has to leave your computer, reach a streaming server, and eventually be delivered to listeners. Understanding this workflow helps explain the different roles played by DJ software and streaming infrastructure.

## From Mixxx to the streaming server

At its simplest, the workflow looks like this:

**Music + microphone → Mixxx → streaming server → listeners**

Mixxx is the **source** of the broadcast. It produces the final audio mix and encodes it before sending it over the Internet.

Depending on the setup, Mixxx can connect directly to an Icecast or Shoutcast server. The broadcasting configuration includes information such as the server address, port, credentials and, for Icecast, a mount point.

The mount point identifies the stream being published on the server. For example, a simplified Icecast setup could look like:

* Host: live.radioking.com

* Port: 80

* Mount: /myradio

Once connected, Mixxx continuously sends the encoded audio to the server.

This distinction is important: **Mixxx produces the stream, while the streaming server distributes it.**

## Why not send the stream directly to listeners?

Imagine a station broadcasting at 128 kbit/s with 100 listeners.

If the broadcaster had to send a separate copy of the stream to every listener, the upload requirement would be roughly: **128 kbit/s × 100 = 12.8 Mbit/s**

With a streaming server, Mixxx only needs to send one stream:

```
                  ┌── Listener
                  │
Mixxx → Server ──┼── Listener
                  │
                  └── Listener
```

The server takes care of the distribution.

This is one of the fundamental differences between the **broadcasting software** and the **streaming infrastructure** . Mixxx needs to reliably produce and send the audio; the server needs to handle the connections from listeners.

## Where does the streaming infrastructure fit?

Once Mixxx has produced the live stream, another layer is needed to make it available to listeners. This is where the streaming infrastructure comes in.

[RadioKing](https://www.radioking.com/) is one example of a hosted streaming platform. In a typical setup, Mixxx sends the encoded stream to RadioKing, which handles its distribution to listeners and provides the infrastructure around the stream:

```
Mixxx

  │ live audio stream
  ▼

RadioKing streaming infrastructure

  │

  ├── Stream

  ├── Metadata

  ├── Web player

  ├── Website / app

  └── Listener connections

```

A platform like RadioKing can also handle automated programming when Mixxx is not connected, as well as features such as audience statistics and different listening endpoints.

Whether the infrastructure is self-hosted with Icecast or Shoutcast, or provided by a service such as RadioKing, the roles remain distinct: **Mixxx produces and sends the live audio, while the streaming infrastructure takes care of distributing it to listeners and providing the services around it.**

## More than just audio

There’s another important part of the stream: **metadata** .

When a track changes, the broadcaster wants the listener to see the artist and title. Mixxx can send this information along with the broadcast, allowing compatible servers and players to display the currently playing track.

So the workflow isn’t just:

**audio → listener**

It’s closer to:

**audio + metadata → streaming infrastructure → player → listener**

This is particularly useful for online radio, where the listening experience often extends beyond the audio itself.

## A simple way to think about the whole workflow

An online radio can be divided into layers:

```
Production
     ↓
Mixxx
     ↓
Streaming
     ↓
Icecast / Shoutcast / hosted infrastructure
     ↓
Listening
     ↓
Player / website / app
```

Mixxx sits at the production end of the chain, but its output is designed to connect to the wider broadcasting ecosystem.

That separation is what makes it possible to use Mixxx with different radio setups, from a small station running its own Icecast server to a larger operation using a hosted streaming infrastructure like RadioKing.

So the next time you click **Start Broadcasting** in Mixxx, keep in mind that there’s quite a bit happening between that button and the moment a listener hears your show.
