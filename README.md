## AnchorFree STF server
Remote control server for Android and iOS devices


## Setup
**Step 1**

Instal and launch locally [RethinkDB](https://rethinkdb.com/docs/install/)

**Step 2**

Install and start the server, which requires Python 3.6 or higher.

First clone the code to the local, use the following method to install the dependency


```bash
pip3 install -r requirements.txt
```

The easiest way to start

```bash
# Start-up mode, which is the easiest method to start
python3 main.py

# Specify the authentication type
python3 main.py --auth simple

# Set the listening port
python3 main.py --port 4000
```

**Step 3: Android device access**

Reference project introduction [atxserver2-android-provider](https://github.com/openatx/atxserver2-android-provider)

**Step 3: iOS device access**

Reference project introduction [atxserver2-ios-provider](https://github.com/openatx/atxserver2-ios-provider)

## Thanks
- <https://github.com/openatx/atxserver2>
- <https://github.com/openstf>
- <https://github.com/Genymobile/scrcpy>
- <https://www.easyicon.net/iconsearch/hub/>
- <https://github.com/mikusjelly/apkutils>
- <https://github.com/gtsystem/python-remotezip>
- <https://github.com/willerce/WhatsInput>

## LICENSE
[MIT](LICENSE)
