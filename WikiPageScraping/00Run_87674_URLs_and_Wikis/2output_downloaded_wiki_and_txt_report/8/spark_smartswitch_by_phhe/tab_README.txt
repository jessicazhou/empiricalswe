[<div class="wiki-body gollum-markdown-content instapaper_body" id="wiki-body">
        <div class="markdown-body">
          <h1>
<a aria-hidden="true" class="anchor" href="#spark-core-firmware--" id="user-content-spark-core-firmware--"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Spark Core Firmware <a href="https://waffle.io/spark/core-firmware" rel="nofollow"><img alt="Backlog" data-canonical-src="https://badge.waffle.io/spark/core-firmware.png?label=backlog&amp;title=backlog" src="https://camo.githubusercontent.com/7efebc1b922cc06833ec615801522f12aeabb0a8/68747470733a2f2f62616467652e776166666c652e696f2f737061726b2f636f72652d6669726d776172652e706e673f6c6162656c3d6261636b6c6f67267469746c653d6261636b6c6f67"/></a> <a href="https://travis-ci.org/spark/firmware" rel="nofollow"><img alt="Build Status" data-canonical-src="https://travis-ci.org/spark/firmware.svg" src="https://camo.githubusercontent.com/ac92ae9ac34352b3facd5a382be9ba4a767d6ad4/68747470733a2f2f7472617669732d63692e6f72672f737061726b2f6669726d776172652e737667"/></a>
</h1>
<p>This is the main source code repository of the Spark Core firmware libraries.</p>
<p>This firmware depends on two other libraries: the <a href="http://www.github.com/spark/core-common-lib">Spark Common Library</a> and the <a href="http://www.github.com/spark/core-communication-lib">Spark Communication Library</a></p>
<ol>
<li><a href="#1-download-and-install-dependencies">Download and Install Dependencies</a></li>
<li><a href="#2-download-and-build-repositories">Download and Build Repositories</a></li>
<li><a href="#3-edit-and-rebuild">Edit and Rebuild</a></li>
<li><a href="#4-flash-it">Flash It!</a></li>
</ol>
<h2>
<a aria-hidden="true" class="anchor" href="#1-download-and-install-dependencies" id="user-content-1-download-and-install-dependencies"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>1. Download and Install Dependencies</h2>
<ol>
<li><a href="#1-gcc-for-arm-cortex-processors">GCC for ARM Cortex processors</a></li>
<li><a href="#2-make">Make</a></li>
<li><a href="#3-device-firmware-upgrade-utilities">Device Firmware Upgrade Utilities</a></li>
<li>
<a href="#4-zatig">Zatig</a> (for windows users only)</li>
<li><a href="#5-git">Git</a></li>
</ol>
<h4>
<a aria-hidden="true" class="anchor" href="#1-gcc-for-arm-cortex-processors" id="user-content-1-gcc-for-arm-cortex-processors"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>1. GCC for ARM Cortex processors</h4>
<p>The Spark Core uses an ARM Cortex M3 CPU based microcontroller. All of the code is built around the GNU GCC toolchain offered and maintained by ARM.</p>
<p>Download and install the latest version from: <a href="https://launchpad.net/gcc-arm-embedded" rel="nofollow">https://launchpad.net/gcc-arm-embedded</a></p>
<p>See <a href="https://gist.github.com/joegoggins/7763637">this Gist</a> for how to get setup on OS X.</p>
<h4>
<a aria-hidden="true" class="anchor" href="#2-make" id="user-content-2-make"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>2. Make</h4>
<p>In order to turn your source code into binaries, you will need a tool called <code>make</code>. Windows users need to explicitly install <code>make</code> on their machines. Make sure you can use it from the terminal window.</p>
<p>Download and install the latest version from: <a href="http://gnuwin32.sourceforge.net/packages/make.htm" rel="nofollow">http://gnuwin32.sourceforge.net/packages/make.htm</a></p>
<h4>
<a aria-hidden="true" class="anchor" href="#3-device-firmware-upgrade-utilities" id="user-content-3-device-firmware-upgrade-utilities"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>3. Device Firmware Upgrade Utilities</h4>
<p>Install dfu-util 0.7. Mac users can install dfu-util with <a href="http://brew.sh/" rel="nofollow">Homebrew</a> or <a href="http://www.macports.org" rel="nofollow">Macports</a>, Linux users may find it in their package manager, and everyone can get it from <a href="http://dfu-util.gnumonks.org/index.html" rel="nofollow">http://dfu-util.gnumonks.org/index.html</a></p>
<h4>
<a aria-hidden="true" class="anchor" href="#4-zatig" id="user-content-4-zatig"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>4. Zatig</h4>
<p>In order for the Core to show up on the dfu list, you need to replace the USB driver with a utility called <a href="http://zadig.akeo.ie/" rel="nofollow">Zadig</a>. Here is a <a href="https://community.spark.io/t/tutorial-installing-dfu-driver-on-windows/3518" rel="nofollow">tutorial</a> on using it. This is only required for Windows users.</p>
<h4>
<a aria-hidden="true" class="anchor" href="#5-git" id="user-content-5-git"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>5. Git</h4>
<p>Download and install Git: <a href="http://git-scm.com/" rel="nofollow">http://git-scm.com/</a></p>
<h2>
<a aria-hidden="true" class="anchor" href="#2-download-and-build-repositories" id="user-content-2-download-and-build-repositories"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>2. Download and Build Repositories</h2>
<p>The entire Spark Core firmware is organized into three repositories. The main firmware is located under <em>core-firmware</em>, while the supporting libraries are subdivided in to <em>core-common-lib</em> and <em>core-communication-lib</em>.</p>
<h4>
<a aria-hidden="true" class="anchor" href="#how-do-we-download-these-repositories" id="user-content-how-do-we-download-these-repositories"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>How do we <em>download</em> these repositories?</h4>
<p>You can access all of the repositories via any git interface or download it directly from the website.</p>
<p>Make sure all of the following repositories are downloaded into the same folder. <em>For example (if all of the repositories are downloaded in a folder called Spark):</em></p>
<pre><code>D:\Spark\core-firmware
D:\Spark\core-common-lib
D:\Spark\core-communication-lib
</code></pre>
<p><em>Method 1: Through the git command line interface.</em></p>
<p>Open up a terminal window, navigate to your destination directory and type the following commands:</p>
<p>(Make sure you have git installed on your machine!)</p>
<ul>
<li><code>git clone https://github.com/spark/core-firmware.git</code></li>
<li><code>git clone https://github.com/spark/core-common-lib.git</code></li>
<li><code>git clone https://github.com/spark/core-communication-lib.git</code></li>
</ul>
<p><em>Method 2: Download the zipped files directly from the Spark's GitHub website</em></p>
<ul>
<li><a href="https://github.com/spark/core-firmware/archive/master.zip">core-firmware</a></li>
<li><a href="https://github.com/spark/core-common-lib/archive/master.zip">core-common-lib</a></li>
<li><a href="https://github.com/spark/core-communication-lib/archive/master.zip">core-communication-lib</a></li>
</ul>
<h4>
<a aria-hidden="true" class="anchor" href="#how-do-we-build-these-repositories" id="user-content-how-do-we-build-these-repositories"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>How do we <em>build</em> these repositories?</h4>
<p>Make sure you have downloaded and installed all the required dependencies as mentioned <a href="#1-download-and-install-dependencies">previously.</a>. Note, if you've downloaded or cloned these previously, you'll want to <code>git pull</code> or redownload all of them before proceeding.</p>
<p>Open up a terminal window, navigate to the build folder under core-firmware
(i.e. <code>cd core-firmware/build</code>) and type:</p>
<pre><code>make
</code></pre>
<p>This will build your main application (<code>core-firmware/src/application.cpp</code>) and required dependencies.</p>
<p><em>For example:</em> <code>D:\Spark\core-firmware\build [master]&gt; make</code></p>
<h4>
<a aria-hidden="true" class="anchor" href="#build-with-the-spark-cli" id="user-content-build-with-the-spark-cli"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Build with the spark-cli</h4>
<pre><code>make &amp;&amp; spark flash COREID core-firmware.bin 
</code></pre>
<h4>
<a aria-hidden="true" class="anchor" href="#linux--mac-serial-connection" id="user-content-linux--mac-serial-connection"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Linux / Mac serial connection</h4>
<p>The following little shell script keeps a screen ready as soon as /dev/tty.usbmodemXXXXX becomes available.</p>
<pre><code>while true; do [ -e /dev/tty.usbmodemXXXXXX ] &amp;&amp; screen -h 500 /dev/tty.usbmodemXXXXXX ; sleep 5; reset; echo "No tty available"; done 
</code></pre>
<h5>
<a aria-hidden="true" class="anchor" href="#common-errors" id="user-content-common-errors"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Common Errors</h5>
<ul>
<li>
<p><code>arm-none-eabi-gcc</code> and other required gcc/arm binaries not in the PATH.
Solution: Add the /bin folder to your $PATH (i.e. <code>export PATH="$PATH:&lt;SOME_GCC_ARM_DIR&gt;/bin</code>).
Google "Add binary to PATH" for more details.</p>
</li>
<li>
<p>You get <code>make: *** No targets specified and no makefile found. Stop.</code>.
Solution: <code>cd core-firmware/build</code>.</p>
</li>
</ul>
<p>Please issue a pull request if you come across similar issues/fixes that trip you up.</p>
<h3>
<a aria-hidden="true" class="anchor" href="#navigating-the-code-base" id="user-content-navigating-the-code-base"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Navigating the code base</h3>
<p>All of the repositories are sub divided into functional folders:</p>
<ol>
<li>
<code>/src</code> holds all the source code files</li>
<li>
<code>/inc</code> holds all the header files</li>
<li>
<code>/build</code> holds the makefile and is also the destination for the compiled <code>.bin</code> and <code>.hex</code> files.</li>
</ol>
<h2>
<a aria-hidden="true" class="anchor" href="#3-edit-and-rebuild" id="user-content-3-edit-and-rebuild"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>3. Edit and Rebuild</h2>
<p>Now that you have your hands on the entire Spark Core firmware, its time to start hacking!</p>
<h3>
<a aria-hidden="true" class="anchor" href="#what-to-edit-and-what-not-to-edit" id="user-content-what-to-edit-and-what-not-to-edit"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>What to edit and what not to edit?</h3>
<p>The main user code sits in the application.cpp file under core-firmware/src/ folder. Unless you know what you are doing, refrain yourself from making changes to any other files.</p>
<p>After you are done editing the files, you can rebuild the repository by running the <code>make</code> command in the <code>core-firmware/build</code> directory. If you have made changes to the other two repositories, make automatically determines which files need to be rebuilt and builds them for you.</p>
<h2>
<a aria-hidden="true" class="anchor" href="#4-flash-it" id="user-content-4-flash-it"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>4. Flash It!</h2>
<p>Its now time to transfer your code to the Spark Core! You can always do this using the Over The Air update feature or, if you like wires, do it over the USB.</p>
<p><em>Make sure you have the <code>dfu-util</code> command installed and available through the command line</em></p>
<h4>
<a aria-hidden="true" class="anchor" href="#steps" id="user-content-steps"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z" fill-rule="evenodd"></path></svg></a>Steps:</h4>
<ol>
<li>
<p>Put you Core into the DFU mode by holding down the MODE button on the Core and then tapping on the RESET button once. Release the MODE button after you start to see the RGB LED flashing in yellow. It's easy to get this one wrong: Make sure you don't let go of the left button until you see flashing yellow, about 3 seconds after you release the right/RESET button. A flash of white then flashing green can happen when you get this wrong. You want flashing yellow.</p>
</li>
<li>
<p>Open up a terminal window on your computer and type this command to find out if the Core indeed being detected correctly.</p>
<p><code>dfu-util -l</code><br/>
you should get the following in return:</p>
<pre><code>Found DFU: [1d50:607f] devnum=0, cfg=1, intf=0, alt=0, name="@Internal Flash  /0x08000000/20*001Ka,108*001Kg" 
Found DFU: [1d50:607f] devnum=0, cfg=1, intf=0, alt=1, name="@SPI Flash : SST25x/0x00000000/512*04Kg"
</code></pre>
<p>(Windows users will need to use the Zatig utility to replace the USB driver as described earlier)</p>
</li>
<li>
<p>Now, navigate to the build folder in your core-firmware repository and use the following command to transfer the <em>.bin</em> file into the Core.</p>
<pre><code>dfu-util -d 1d50:607f -a 0 -s 0x08005000:leave -D core-firmware.bin
</code></pre>
<p>For example, this is how my terminal looks like:</p>
<pre><code></code></pre>
</li>
</ol>
<p>D:\Spark\core-firmware\build [master]&gt; dfu-util -d 1d50:607f -a 0 -s 0x08005000:leave -D core-firmware.bin</p>
<pre><code>Upon successful transfer, the Core will automatically reset and start the running the program.

##### Common Errors
* As of 12/4/13, you will likely see `Error during download get_status` as the last line from 
the `dfu-util` command. You can ignore this message for now.  We're not sure what this error is all about.

* If you are having trouble with dfu-util, (like invalid dfuse address), try a newer version of dfu-util. v0.7 works well.

**Still having troubles?** Checkout our [resources page](https://www.spark.io/resources), hit us up on IRC, etc.

### CREDITS AND ATTRIBUTIONS

The Spark application team: Zachary Crockett, Satish Nair, Zach Supalla, David Middlecamp and Mohit Bhoite.

The core-firmware uses the GNU GCC toolchain for ARM Cortex-M processors, ARM's CMSIS libraries, TI's CC3000 host driver libraries, STM32 standard peripheral libraries and Arduino's implementation of Wiring.

### LICENSE

Unless stated elsewhere, file headers or otherwise, all files herein are licensed under an LGPLv3 license. For more information, please read the LICENSE file.

### CONTRIBUTE

Want to contribute to the Spark Core project? Follow [this link]() to find out how.

### CONNECT

Having problems or have awesome suggestions? Connect with us [here.](https://community.sparkdevices.com/)

### VERSION HISTORY

Latest Version: v1.0.0
</code></pre>

        </div>

    </div>]