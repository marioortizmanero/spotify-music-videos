<div align="center">

<img src="images/logo.png" height=100 alt="logo" align="center"/>
<h1>Spotivids</h1>

<span>Watch Youtube <b>music videos</b> and <b>lyrics</b> for the currently playing Spotify songs</span>

<img alt="Travis" src="https://travis-ci.com/marioortizmanero/spotivids.svg?branch=master"> <img alt="PyPi version" src="https://img.shields.io/pypi/v/spotivids"> <img alt="AUR version" src="https://img.shields.io/aur/version/spotivids">

<hr>

<img src="images/screenshot.png" alt="Example" align="center">

</div>


## Table of contents
* [Requirements](#requirements)
* [Installation](#installation)
* [Usage and configuration](#usage)
    * [Basic usage](#usage)
    * [Advanced](#advanced)
    * [The config file](#the-config-file)
* [The web API](#the-web-api)
    * [Obtaining your client ID and client secret](#obtaining-your-client-id-and-client-secret)
* [Development resources](#development)
    * [Tests](#tests)
    * [Current Limitations](#current-limitations)


## Requirements
* Python 3.7+
* VLC or mpv to play the videos

For **Linux** users:

* [PyGI](https://pygobject.readthedocs.io/en/latest/) (not packaged on PyPi, you need to install it from your distribution's repository - it's usually called python-gi, python-gobject or pygobject). Here's a quick [tutorial](https://pygobject.readthedocs.io/en/latest/getting_started.html) on how to install it on most systems.

* [GLib](https://developer.gnome.org/glib/). You most likely have it installed already.


## Installation
* You can use pip to install it: `pip3 install spotivids --user`. If you want to use mpv instead of VLC, just use `pip3 install 'spotivids[mpv]' --user` instead.

* You can download the latest stable [release](https://github.com/marioortizmanero/spotivids/releases). There should be binaries avaliable for Mac OS, Linux and Windows. These already include mpv support.

* If you're on Arch Linux, you can install it from the AUR: [`spotivids`](https://aur.archlinux.org/packages/spotivids/). Install [python-mpv](https://aur.archlinux.org/packages/python-mpv/) for mpv support.


## Usage
I'm working towards making this program a full GUI with as little interaction with the terminal as possible. The GUI should be intuitive enough to not need a tutorial. But you can still combine the terminal usage with the GUI:

```
usage: spotivids [-h] [-v] [--debug] [--config-file CONFIG_PATH] [-n] [-f]
                 [--use-mpv] [--width WIDTH] [--height HEIGHT] [-w]
                 [--client-id CLIENT_ID] [--client-secret CLIENT_SECRET]
                 [--redirect-uri REDIRECT_URI] [--vlc-args VLC_ARGS]
                 [--mpv-flags MPV_FLAGS]
```

| Argument                         | Description         |
|----------------------------------|---------------------|
| `-n`, `--no-lyrics`              | do not print lyrics. |
| `-f`, `--fullscreen`             | play videos in fullscreen mode. |
| `--stay-on-top`                  | the window will stay on top of other apps. |
| `--width <WIDTH>`                | set the width for the downloaded videos (this is useful to play low quality videos if your connection isn't good). |
| `--height <HEIGHT>`              | set the height for the downloaded videos. |
| `--use-mpv`                      | use [mpv](https://mpv.io/) instead of [VLC](https://www.videolan.org/vlc/index.html) to play videos. Note: requires `python-mpv`, see the [installation section](#installation) for more. |
| `-w, --use-web-api`              | use Spotify's web API. See [the web API section](#the-web-api) for more info about how to set it up. |

### Advanced:
| Argument                         | Description         |
|----------------------------------|---------------------|
| `--config-file <PATH>`           | indicate the path of your config file.  |
| `--vlc-args <VLC_ARGS>`          | custom arguments used when opening VLC. Note that some like `args='--fullscreen'` won't work in here |
| `--mpv-flags <MPV_ARGS>`         | custom boolean flags used when opening mpv, with dashes and separated by spaces. Not intended for customization, only debugging and simple things. If you want to load non-boolean flags and such, use a config file. |
| `--client-id <CLIENT_ID>`        | your client ID. Mandatory if the web API is being used. Check the [web API section](#the-web-api) to learn how to obtain yours. You can also use the GUI to input it. |
| `--client-secret <CLIENT_SECRET>`| your client secret ID. Mandatory if the web API is being used. Check the [web API section](#the-web-api) to learn how to obtain yours. You can also use the GUI to indicate it. |
| `--redirect-uri <REDIRECT_URI>`| optional redirect uri to get the web API authorization token. The default is http://localhost:8888/callback/ |

### The config file
The config file is created by default at your usual config directory:
* Unix: `~/.config/spotivids/config.ini` (or in `$XDG_CONFIG_HOME`, if defined)
* Mac OS X: `~/Library/Preferences/spotivids/config.ini`
* Windows: `C:\Users\trentm\AppData\Local\spotivids\config.ini`

You can use a custom one by passing `--config-file <PATH>` as an argument. The config file is overriden by the configuration passed as arguments. [Here's an example of one](https://github.com/marioortizmanero/spotivids/blob/master/example.ini). It uses the [INI config file formatting](https://en.wikipedia.org/wiki/INI_file). Most options are inside the `[Defaults]` section. The web API related options are inside `[WebAPI]`.

All the available options for the config file are the same as the arguments listed in the [Usage section](#usage), except for `--config-file <PATH>`, which is only an argument. Their names are the same but with underscores instead of dashes. For example, `--use-mpv` would be equivalent to `use_mpv = true`.

Some other options are only avaliable on the config file, like `auth_token` and `expiration`, but these are only used to retain info from the WebAPI and should not be modified manually.


## The web API
All platforms have a local way to get metadata from Spotify, but it may not be as reliable as the official web API, or may lack features in comparison to it, like better audio syncing or pausing the video. However, it also brings other downsides:

* You have to sign in and set it up manually
* Only Spotify Premium users are able to use some functions
* API calls are limited

The simplest way to use the web API is by passing `--use-web-api` as an argument and following the instructions in the GUI to get access.

You can also enable it directly from the config file. Example of the section inside the config file:

```ini
[WebAPI]
use_web_api = true
client_id = 5fe01282e44241328a84e7c5cc169165
client_secret = 2665f6d143be47c1bc9ff284e9dfb350
```

Finally, you can use arguments: `spotivids -w --client-id <CLIENT_ID> --client-secret <CLIENT_SECRET>`. They will be saved in the default config file later. `auth_token` and `expiration` will be written into the config file too, but do not touch these.

### Obtaining your client ID and client secret:
1. Go to the [Spotify Developers Dashboard](https://developer.spotify.com/dashboard/applications)
2. Create a new client ID. You can fill the descriptions as you like. Select `No` when asked if it's a commercial integration and accept the Terms and Conditions in the next step.
3. Go to `Edit Settings` and type `http://localhost:8888/callback/` (the default redirect uri) in the Redirect URIs field.
4. You can now copy your Client ID and Client Secret and add them when you call `spotivids` by passing them as arguments or saving it directly into your config file, as shown above.

You will be prompted to paste the resulting URL that was opened in your browser into the program. It will be a broken website but all you need is the URL. After doing it, the authorization process will be complete. The auth info will be saved into the config file for future usage.

---

## Development
Helpful documentation links for contributing:
* [DBus](https://dbus.freedesktop.org/doc/dbus-specification.html), [pydbus](https://github.com/LEW21/pydbus), [MPRIS](https://specifications.freedesktop.org/mpris-spec/latest/Player_Interface.html#Property:Position), [Qt for Python](https://wiki.qt.io/Qt_for_Python).
* [python-vlc](https://www.olivieraubert.net/vlc/python-ctypes/doc/), [python-mpv](https://github.com/jaseg/python-mpv).

The app logo was created by [xypnox](https://github.com/xypnox) in this [issue](https://github.com/marioortizmanero/spotivids/issues/26).

The changelog and more information about this program's versions can be found in the [Releases page](https://github.com/marioortizmanero/spotivids/releases).

Inside `dev/` you can find more information about building: [BUILDING.md](https://github.com/marioortizmanero/spotify-music-videos/blob/master/dev/BUILDING.md).

### Tests
You can run the module locally with `python -m spotivids`.

This project uses `unittest` for testing. Run them with `python -m unittest` or `python -m unittest discover -s tests`

### Current limitations
* Spotify on Linux doesn't currently support the MPRIS property `Position` so the starting offset is calculated manually and may be a bit rough.
* Spotify's Web API doesn't allow function calls on updates like DBus, meaning that the metadata has to be manually updated every second and checked in case of changes.
* A server is needed to get a working `redirect_uri` and a much easier Spotify login. So a website should be created in the future, rather than implementing it with flask on localhost only because of this. But it require some funding to host the site.
