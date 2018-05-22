[<div class="wiki-body gollum-markdown-content instapaper_body" id="wiki-body">
        <div class="markdown-body">
          <p>ExaBGP can be controlled using signal. Configuration changes can be notified to the program using signals:</p>
<p>Supported signals are :</p>
<ul>
<li>SIGALRM : restart ExaBGP</li>
<li>SIGUSR1 : reload the configuration</li>
<li>SIGUSR2 : reload the configuration and the forked processes</li>
<li>SIGTERM : terminate ExaBGP</li>
<li>SIGHUP  : terminate ExaBGP (does NOT reload the configuration anymore to allow to run ExaBGP under screen)</li>
</ul>
<p><strong>Reloading large configuration using signal is <em>not</em> recommended</strong> as the configuration parsing code is currently blocking (as well as some part of the RIB required for the reload - for simplicity).</p>
<p>Therefore if you have large configuration change, it could cause the peer to miss some keepalive and cause a flap.</p>

        </div>

    </div>]