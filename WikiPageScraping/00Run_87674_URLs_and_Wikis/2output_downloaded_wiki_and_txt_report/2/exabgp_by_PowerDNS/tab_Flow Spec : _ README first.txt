[<div class="wiki-body gollum-markdown-content instapaper_body" id="wiki-body">
        <div class="markdown-body">
          <p>Before using flowspec :</p>
<ul>
<li>take note that <a href="https://support.cloudflare.com/hc/en-us/articles/200172446-CloudFlare-Post-Mortem-from-Outage-on-March-3-2013" rel="nofollow">flowspec does not like human errors</a>
</li>
<li>read <a href="http://mailman.nanog.org/pipermail/nanog/2011-January/030051.html" rel="nofollow">how complex flows can break your network</a>
</li>
<li>shake your head and notice that Juniper currently treat the data as BITS per seconds and not BYTES per seconds as required by the RFC - well until it was fixed with PR864496</li>
<li>offset support for IPv6 is not supported by all hardware
<ul>
<li>Alcatel Lucent 7750 SR with SR OS ver 11.0R5 does not support it</li>
<li>Cisco : no information</li>
<li>Juniper : no information</li>
</ul>
</li>
</ul>

        </div>

    </div>]