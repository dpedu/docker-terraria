docker-terraria
===============

Terraria (tshock) under Mono in a docker container.

Reccomended usage:

`docker run -d -p 7777:7777 -p 7878:7878 -v /host/terraria_data/:/opt/terraria/tshock/ terraria`

To enable RPC, *config.json* must be copied to `/host/terraria_data/`.

Env vars
--------

* `WORLDSIZE` - default 1, can be 2 or 3 for small/med/large worlds
* `WORLDFILENAME` - default "terraria.wld", name for the world save file

Admin cli
---------

Included is an admin tool for interacting with a server.

First-time setup:

* `trcli -a mkuser`

Per-run token generation:

* `trcli -a gettoken`

Execute arbitrary commads:

* `trcli -a cmd -c '/protectspawn'v

