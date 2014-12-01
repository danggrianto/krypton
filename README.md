# KRYPTON

## Intro

Krypton is an extension of selenium webdriver. We can say that krypton is a framework for running automated test.


## Config File

Krypton needs a config file in the system to run.

`export KRYPTON_CONFIG='path/to/config'`

Example of the config file:

```
{
    "application": {
        "protocol": "http",
        "url": "localhost",
        "port": 80
    },
    "selenium": {
        "remote": false,
        "browser": "FIREFOX",
        "version": "ANY",
        "platform": "MAC",
        "hub" : {
          "provider": "local",
          "url": "localhost",
          "port": "4444"
        }
    }
}
```

