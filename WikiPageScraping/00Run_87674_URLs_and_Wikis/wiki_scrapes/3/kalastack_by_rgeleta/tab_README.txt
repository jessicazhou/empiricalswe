[<div class="wiki-body gollum-markdown-content instapaper_body" id="wiki-body">
        <div class="markdown-body">
          <h1>
<a aria-hidden="true" class="anchor" href="#kalastack-3" id="user-content-kalastack-3"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Kalastack 3!</h1>
<p>Kalastack is a basic LEMP stack built for Drupal. At its core it is a series of puppet manifests that
are managed by Vagrant. Kalastack was built to run primarily on Ubuntu Server 12.04, though it will welcome multiple architectures in the future.</p>
<p>If you are interested in support for other architectures check out <a href="https://github.com/proviso/proviso">Proviso</a></p>
<h2>
<a aria-hidden="true" class="anchor" href="#installation" id="user-content-installation"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Installation</h2>
<p>Kalastack 3 requires at least <a href="http://downloads.vagrantup.com/tags/v1.3.5" rel="nofollow">Vagrant 1.3.5</a> and <a href="http://download.virtualbox.org/virtualbox/4.2.18/" rel="nofollow">VirtualBox 4.2.18</a> to be run correctly. Before you begin please download both. If you are upgrading to Vagrant 1.5 you may need to go through the Vagrant update process.</p>
<p><strong>System Requirements:</strong></p>
<ul>
<li>Kalastack works on both 64 and 32 bit architectures and requires at least 2GB of ram.</li>
</ul>
<p><em>Notes:</em> At this time, Kalastack is actively tested on Mac OSX 10.9 and with Vagrant 1.6.3 and VirtualBox 4.3.12. It has also been used on Ubuntu 12.04 both natively and using VirtualBox and Vagrant. You may have to play around with the VT Intel settings on your machine to get it to work. That all said it is not a recommended or supported environment at this time.</p>
<p>*More Notes: On Ubuntu 12.04 with a Kernel of 3.9.0-x or greater, you may have issues with the 4.2.18 VBnot working properly.  This is resolved by using the a version of 4.3.x.</p>
<p>Once you have downloaded and installed both Vagrant and VirtualBox,
you can build out the complete stack:</p>
<div class="highlight highlight-source-shell"><pre>$ mkdir <span class="pl-k">~</span>/kalastack
$ <span class="pl-c1">cd</span> <span class="pl-k">~</span>/kalastack
$ git clone git://github.com/kalamuna/kalastack.git ./
  (or download and expand the latest 3.x tarball from https://github.com/kalamuna/kalastack/tags)
$ vagrant plugin install vagrant-hostsupdater
$ vagrant up</pre></div>
<p>You should now be able to access <a href="http://start.kala" rel="nofollow">http://start.kala</a> in your browser!</p>
<p>To ssh into your server, from within ~/kalastack, issue:</p>
<div class="highlight highlight-source-shell"><pre>$ vagrant ssh</pre></div>
<h2>
<a aria-hidden="true" class="anchor" href="#upgrading-from-kalastack-2" id="user-content-upgrading-from-kalastack-2"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Upgrading from Kalastack 2</h2>
<p>Theoretically this should work but it hasn't been tested but here are the steps.</p>
<ol>
<li>Upgrade your VirtualBox and Vagrant to at least the correct versions.   <a href="http://downloads.vagrantup.com/tags/v1.3.5" rel="nofollow">Vagrant 1.3.5</a> and <a href="http://download.virtualbox.org/virtualbox/4.2.18/" rel="nofollow">VirtualBox 4.2.18</a>
</li>
<li>Checkout the latest version of 3.x aka</li>
</ol>
<div class="highlight highlight-source-shell"><pre>$ <span class="pl-c1">cd</span> <span class="pl-k">~</span>/kalastack
$ git fetch --all <span class="pl-c"><span class="pl-c">#</span>This will grab the new branch</span>
$ git checkout 3.x
  (or download and expand the latest 3.x tarball from https://github.com/kalamuna/kalastack/tags)
$ vagrant up --provison</pre></div>
<p>Please contact us on whether this works or doesn't.</p>
<h2>
<a aria-hidden="true" class="anchor" href="#post-install-checks" id="user-content-post-install-checks"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Post Install Checks</h2>
<h3>
<a aria-hidden="true" class="anchor" href="#your-files" id="user-content-your-files"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>YOUR FILES</h3>
<p>Kalastack uses NFS file sharing. You can access your server webroot at ~/kalabox/www on your host
machine. This way you can use your local IDE to edit files on your server.</p>
<h2>
<a aria-hidden="true" class="anchor" href="#working-with-kalastack" id="user-content-working-with-kalastack"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Working with Kalastack</h2>
<p>###Start/Stop</p>
<p>Don't start the box in Virualbox, but instead, from within the kalastack codebase use the command line to spin up the stack:</p>
<div class="highlight highlight-source-shell"><pre>$ vagrant up</pre></div>
<p>and log in via:</p>
<div class="highlight highlight-source-shell"><pre>$ vagrant ssh</pre></div>
<p>and spin down the box with:</p>
<div class="highlight highlight-source-shell"><pre>$ vagrant halt</pre></div>
<h2>
<a aria-hidden="true" class="anchor" href="#working-with-pantheon" id="user-content-working-with-pantheon"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Working with Pantheon</h2>
<p>Kalastack makes use of the <a href="https://github.com/kalamuna/terminatur">Terminatur</a> which is built on top of the amazing <a href="https://github.com/pantheon-systems/terminus">Terminus</a>. Please
consult the <a href="https://github.com/kalamuna/terminatur">Terminatur Documentation</a> for a complete run down on how to use Kalastack with your Pantheon sites.</p>
<h3>
<a aria-hidden="true" class="anchor" href="#updating-your-host-hosts-file" id="user-content-updating-your-host-hosts-file"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>UPDATING YOUR HOST HOSTS FILE</h3>
<p>Remember that the Kalastack does not automatically update the /etc/hosts file on
your host machine, so you'll need add each new site manually in order
to visit <a href="http://SITENAME.kala" rel="nofollow">http://SITENAME.kala</a> in your web browser! Kalastack does, however, manage the hosts
file in your VM.</p>
<p>1.3.3.7    SITENAME.kala</p>
<h2>
<a aria-hidden="true" class="anchor" href="#xdebug" id="user-content-xdebug"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Xdebug</h2>
<p>Kalastack ships with xdebug for both debugging and profiling.</p>
<h3>
<a aria-hidden="true" class="anchor" href="#debugging" id="user-content-debugging"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>DEBUGGING</h3>
<p>Debugging is best done with an IDE such as netbeans or eclipse or with a text editor such as SublimeText.</p>
<p>The xdebug setup should already be done on the Kalastack end so you should
only need to set up your IDE. Here is some useful documentation for <a href="http://brianfisher.name/content/drupal-development-environment-os-x-mamp-pro-eclipse-xdebug-and-drush" rel="nofollow">eclipse</a>, <a href="http://wiki.netbeans.org/HowToConfigureXDebug" rel="nofollow">netbeans</a> and
<a href="https://github.com/martomo/SublimeTextXdebug">SublimeText</a>.</p>
<h3>
<a aria-hidden="true" class="anchor" href="#profiling" id="user-content-profiling"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>PROFILING</h3>
<p>For profiling, we recommend you use the webgrind client which comes preconfigured
with your Kalastack and is located at <a href="http://grind.kala" rel="nofollow">http://grind.kala</a>.</p>
<p>Profiling on every page has a performance impact so you must trigger what pages
you want to profile by manually appending ?XDEBUG_PROFILE to
the URL (see <a href="http://xdebug.org/docs/profiler" rel="nofollow">xdebug documentation</a> for more detail) and then
checking <a href="http://grind.kala" rel="nofollow">webgrind</a>.</p>
<p>Many browsers also offer automated tools/plugins to turn profiling on and off, i.e. <a href="https://chrome.google.com/webstore/detail/xdebug-helper/eadndfjplgieldjbigjakmdgkmoaaaoc" rel="nofollow">Xdebug helper</a> for google Chrome.</p>
<h3>
<a aria-hidden="true" class="anchor" href="#apache-solr" id="user-content-apache-solr"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>APACHE SOLR</h3>
<p>Currently, Kalastack doesn't come with Solr installed by default. You can, however,
easily add it in by following the instructions on the <a href="https://github.com/kalamuna/kalastack/wiki/Adding-Solr-to-Kalastack">Adding Solr wiki page</a>.</p>
<h3>
<a aria-hidden="true" class="anchor" href="#frontend-tooling" id="user-content-frontend-tooling"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>FRONTEND TOOLING</h3>
<p>Currently, Kalastack doesn't come with front end tooling like <code>grunt</code>, <code>bower</code>, <code>sass</code>, <code>compass</code> and <code>yo</code> installed by default.
You can, however, easily add it in by following the instructions on the <a href="https://github.com/kalamuna/kalastack/wiki/Adding-front-end-tooling">Adding front end tooling</a>.</p>
<hr/>
<p>(C) 2014 Kalamuna LLC</p>

        </div>

        <div class="wiki-footer gollum-markdown-content boxed-group" id="wiki-footer">
          <div class="boxed-group-inner wiki-auxiliary-content markdown-body">
            <p>Copyright © 2014 Kalamuna, LLC</p>

          </div>
        </div>
    </div>]