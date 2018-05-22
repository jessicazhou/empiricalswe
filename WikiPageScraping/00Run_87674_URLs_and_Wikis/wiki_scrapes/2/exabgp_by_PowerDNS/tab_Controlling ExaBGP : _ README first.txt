[<div class="wiki-body gollum-markdown-content instapaper_body" id="wiki-body">
        <div class="markdown-body">
          <h3>
<a aria-hidden="true" class="anchor" href="#overview" id="user-content-overview"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Overview</h3>
<p>ExaBGP was designed to be controlled from third party applications. Your application will be launched by ExaBGP which will then interact with it.</p>
<p>Two API are currently available to do so, the text API (more exhaustive) and its JSON conterpart (more recent but the way to go).</p>
<p>The way for a program to use the API is by reading from STDIN ( like if the command were entered using the keyboard ) and writing to STDOUT, like printing on the screen.</p>
<p>From version 3.3.0, the version reported in the JSON message reflect the last version at which a change was performed. Change must not be expected to always be backward compatible and the CHANGELOG (and this wiki) be looked at to understand the changes performed.</p>
<h3>
<a aria-hidden="true" class="anchor" href="#example-availables" id="user-content-example-availables"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Example availables</h3>
<p>Many examples are available in the example folder of ExaBGP, or the dev folder where the feature is use extensively for performing tests.</p>
<p>I will demonstrate how to use the feature using one of the test defined by the files exabgp/dev/runtest/api-add-remove.conf and exabgp/dev/runtest/api-add-remove.run</p>
<h3>
<a aria-hidden="true" class="anchor" href="#configuring-exabgp-to-use-your-program" id="user-content-configuring-exabgp-to-use-your-program"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Configuring ExaBGP to use your program.</h3>
<pre><code>neighbor 127.0.0.1 {
	router-id 1.2.3.4;
	local-address 127.0.0.1;
	local-as 1;
	peer-as 1;
	graceful-restart;

	process announce-routes {
		run ./api-add-remove.run;
	}
}
</code></pre>
<p>The name "announce-routes" is just an informational string (which must not contain any spaces or tabulations).</p>
<p>The section "process" defined the program which is going to be run by ExaBGP. The path can be absolute or relative to the configuration file location.</p>
<h3>
<a aria-hidden="true" class="anchor" href="#the-controlling-application" id="user-content-the-controlling-application"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>The controlling application</h3>
<pre><code>#!/usr/bin/env python

import sys
import time

messages = [
'announce route 1.1.0.0/24 next-hop 101.1.101.1',
'announce route 1.1.0.0/25 next-hop 101.1.101.1',
'withdraw route 1.1.0.0/24 next-hop 101.1.101.1',
]

time.sleep(2)

while messages:
	message = messages.pop(0)
	sys.stdout.write( message + '\n')
	sys.stdout.flush()
	time.sleep(1)

while True:
	time.sleep(1)
</code></pre>
<p>This program will print three command to be executed by ExaBGP, announce a route, another and then ask for the first route to be withdrawn and then will then wait for termination.</p>
<h3>
<a aria-hidden="true" class="anchor" href="#important-note" id="user-content-important-note"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Important note</h3>
<p>Implementators using this API should keep in mind that read on STDIN are normally blocking. When using the same process for SENDING and receiving, ASYNC IO programming techniques should be used.</p>
<p>However two processes, one for sending and one for receiving, can be used, which may make the programming task easier if shared states are stored in a common database / key store / NoSQL application.</p>

        </div>

    </div>]