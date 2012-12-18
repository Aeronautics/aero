====
aero
====

The **aero** command line package recycler. It uses package managers you already have.

Instead of having to consult several package managers when you are looking for something you can now search through all of them using the same commands and find similar results using the same tool.

When you type ``aero search php``, **aero** already knows which package managers are installed and starts collecting information from each package manager while caching the results for when you haven't found exactly what you're looking for yet. Other advanced features besides caching includes intuitive help and command line arguments parsing, loading configurations from file, bash and zsh autocompletion, results paging so that you don't have to always scroll up when the information you need is right at the top of the results that just came flying by but you also wont get dumped into a pager, of your choice I should add, if the results would fit on a single page and doesn't require paging. These are just some of the features already incorporated to enhance your user experience setting new standards for enjoyable software management.

Even though **aero** is some serious machining it will only focus on the task its set out to do, to recycle your existing package managers and you can rest assured/or continue to worry whichever might be the case, as **aero** will leave the heavy lifting up to the software partners already tasked with the use case requirements and instead only focuses on the end user requirements through consistent interfaces, intuitive interactions and all the information you require at your fingertips enabling you to make the decisions you need to accomplish the tasks at hand.::


	   \
	    \
	     \ \    .           _____    ___________  ____
	      \_\__/            \__  \ _/ __ \_  __ \/  _ \
	     O__| \ \            / __ \\  ___/|  | \(  <_> )
	        \ o\/           (____  /\___  >__|   \____/
	         \_/\                \/     \/
	         / \ \
	         O  \                                          aero v0.0.1 alpha 2
	    _________\_____________________________________________________
	              \
	               \


Platform
--------

Written in python using v 2.7, this may or may not be the entry requirement for now, on Mac OS X currently and the excellent IDE [PyCharm by JetBrains](http://www.jetbrains.com/pycharm/) which you may consider highly recommended do give it a try. The *nixes will likely be included soon, there exists no bias to the MS platforms only less accessible as a product of choice and opportunity I guess. Feel free to suggest other usages or specific requirements you might have.

After some serious deliberations even though the majority of the team has zero to no python experience at all it will never the less prevent us, like the good professional programmers we are, from using the best hammer for hitting the particular nails or fingers. This has been an interesting learning curve so far and I have to agree python is a pleasure and does suite the requirements like a glove and now that we are empowered with some new lingo like "pythonic" and "tupels" not to mention "generators" and the other "PEP" "recipes" of convenience we make no claim that this is an exemplary python implementation but we sure as the indents are important will try. Feel free to pin-point any obvious mistakes by raising an issue so we may apologise or be damned to continue in err without permission as we continue under assumption that this is the pythonic way. Now I guess I should go read the book perhaps =)


Disclaimer
----------

Even though using **aero** can cause you or your system no harm, by design and while we are using it everyday for a one stop interface to finding the software we need to install we need to warn you about two things:

1. This is still a work in progress and you are welcome to pitch in, lend a hand, test, report bugs, request features or make a donation but keep in mind that you will find unfinished and more than likely some broken things.
2. May lead to compulsive package installation disorders can cause dependency and some serious addictions, use at your own risk.

Installation
------------

+ aero install with pip (egg and chicken)

Aero installation if you already have aero - from version 0.0.1a1 pip will always reinstall

    $ aero install pip:https://github.com/Aeronautics/aero/tarball/develop

+ aero install with pip --upgrade - upgrade aero and dependencies  - from version 0.0.1a1

    $ aero install pip:https://github.com/Aeronautics/aero/tarball/develop --- "--upgrade https://github.com/Aeronautics/aero/tarball/develop"

+ pip installation

aero can be installed directly from github via pip with the following command:

    $ pip install --upgrade https://github.com/Aeronautics/aero/tarball/develop

+ through easy_install

if you prefer using easy_install the following command will download and install aero from github

    $ easy_install https://github.com/Aeronautics/aero/tarball/develop

+ From git repository:

Clone the repo from github or fork it first and then clone your copy if you want to help out with pull requests. Then just run the setup.py with install:

    $ ./setup.py install

Don't forget to enable autocompletion support, aero will generate the appropriate script to add to you .profile for either bash or zsh support.

For bash

```
    $ aero --completion bash >> ~/.profile
```

For zsh

```
    $ aero --completion zsh >> ~/.profile
```

Alternatively you can use eval on the script to have the shell activated on execution:

```
    $ eval "$(aero -c bash)"
```

Running the aero.py executable from the root package folder also works and may be symlinked in your path if you need another approach while we iron out the kinks.

Running aero:
------------
On execution of **aero** with no requirements a short usage instruction will be presented::

    $ aero

    aero v0.0.1 alpha 0

    usage: aero [-h] [-v] [-p PAGER] [-d [{Brew,Port,Pip,Npm,Gem,Colour}]] [-i]
                  [-c {bash,zsh}]
                  command [mngr:] package ...
    aero: error: too few arguments

Providing **aero** with the customary ``--help`` argument will give more detailed information::

    $ aero --help

	    ____________________
	 __/ Usage Instructions \___________________________________________________
	|___________________________________________________________________________|

	 aero [-h] [-v] [-p PAGER] [-d [{npm,pyrus,pear,pip,brew,pecl,gem}]]
	            [-i] [--- PASSTHRU] [-c {bash,zsh}]
	            command [mngr:]package ...

	    ____________________
	 __/  Argument Options  \___________________________________________________
	|___________________________________________________________________________|

	optional arguments:
	  -h, --help            show this help message and exit
	  -v, --version         Show program's version number and exit
	  -p, --pager PAGER     The pager to use for long paged displays. The default
	                        is based on the environment variable $PAGER, if it is
	                        not set, some common pagers like "less", "more",
	                        "most" and finally "cat" are tried, in this order.

	                        default: /usr/bin/less

	  -d, --disable [{npm,pyrus,pear,pip,brew,pecl,gem}]

	                        Add the items you wish to disable to the list.
	                        Multiple disable arguments may be supplied.

	                        default: []

	  -i, --invalidate-cache
	                        Clear the search cache and enquire anew from the
	                        package managers.

	                        default: False

	  ---, --pass-through PASSTHRU
	                        Passthru arguments to be added as arguments to the
	                        package manager's command execution. Enclose the
	                        arguments in quotes to distinguish them from others.

	                        default: None

	  -c, --completion {bash,zsh}
	                        Command auto completion is supported for both bash and
	                        zsh. The result from the completion option can be
	                        appended to your .profile or simply using eval. ex. `
	                        aero --completion zsh >> ~/.profile` Remember to
	                        source the changes. To use eval you might try
	                        something like: ex. ` eval "$(aero --completion
	                        bash)"`

	                        default: None


	    __________________
	 __/  Commands Usage  \_____________________________________________________
	|___________________________________________________________________________|

	Command arguments:

	  The aero commands are based on the typical package manager
	  commands followed by the package name(s) to perform the task on.
	  At least one command is required but several packages can be
	  processed simultaneously.
	  Use "aero command --help" to get further details for specific
	  commands.

	  command [mngr:]package
	                        Optionally provide the specific manager to use
	                        prepended to the package name(s) with a colon ":" or
	                        alternatively aero will execute the command against
	                        all enabled package managers.

	    choose one of the following valid aero commands:

	    info                Do an aero info for a package
	    search              Do an aero search for a package
	    install             Do an aero install package

	Configuration argument:

	  It is possible to load aero configuration from an input file.

	  @filename             Append "key, value" (where applicable) to a file one
	                        argument, value pair per line. To tell aero which
	                        file to use for configuration specify the path and
	                        file name prefixed with an "@".

Commands
--------

With **aero** you can expect to use the common commands and we will translate them to the package manager specific instructions where they may have chosen to deviate from the norm. Currently the following commands are implemented:

Usage:

```
    $ aero <command> <packages...>
```

Where packages are one or more package names optionally prefixed with the specific package manager, colon separated. The ``mngr:package`` format produced in search is used to instruct a specific package manager with any commands. Omitting the prefix instruction will result in all active package managers being instructed to complete the task. This may or may not necessarily have the desired effect. Multiple packages from different package managers can all be processed with one aero command.

* search
To search for a package which will produce a list with the package manager prefixed the package name by ":" and a short description of the package.
* install
To instruct the installation of a given package.
* info
To obtain more detailed information regarding a given package now also available for pip.

Package managers
================

The following package managers has been enabled, more will follow:

Homebrew
--------
Supported commands:

* search
* install
* info

```
$ aero search brew:ncurses

────────────────────────────────────────────────────────────────────────────────
                 PACKAGE NAME   DESCRIPTION
──────────────────────────────┬─────────────────────────────────────────────────
                 brew:ncurses │ version:stable 5.9
                              │ http://www.gnu.org/s/ncurses/
                              │ /usr/local/Cellar/ncurses/5.9 (1777 files,
                              │ 18M) *
──────────────────────────────┴─────────────────────────────────────────────────

$ aero info brew:ncurses

────────────────────────────────────────────────────────────────────────────────
                 INFORMATION:   ncurses
──────────────────────────────┬─────────────────────────────────────────────────
                     version: │ stable 5.9
                              │ http://www.gnu.org/s/ncurses/
                              │ /usr/local/Cellar/ncurses/5.9 (1777 files,
                              │ 18M) *
                              │ ==> Options
                              │ --universal
                              │ Build a universal binary
──────────────────────────────┴─────────────────────────────────────────────────

```

Special notes:

Brew has the inclination to only return the package names on search, in addition to retrieval of the package names aero continues to further query info on each package from where it is able to parse and present slightly more usable information. Instead of just calling the info command on the package manager we execute `aero info` instead which means that all the information for every package listed in the search results is already cached and retrievable instantaneously.

Gem
---
Supported commands:

* search
* install
* info

```
$ aero search gem:fibonacci

────────────────────────────────────────────────────────────────────────────────
                 PACKAGE NAME   DESCRIPTION
──────────────────────────────┬─────────────────────────────────────────────────
        gem:closest-fibonacci │ Version: 0.1.2
                              │ http://github.com/kevindickerson/closest-
                              │ fibonacci
                              │ Provides some methods to find a Fibonacci
                              │ number less than a given N.
    gem:closest-fibonacci-gem │ Version: 1.1.0
                              │ http://github.com/beckram23/closest-
                              │ fibonacci-gem
                              │ Find the largest fibonacci that is smaller
                              │ than the given integer
        gem:closest_fibonacci │ Version: 1.2.13
                              │ http://github.com/bpolania/closest_fibonacci
                              │ Fibonacci gem for ModCloth
                gem:fibonacci │ Version: 0.1.7
                              │ http://github.com/chaitanyav/fibonacci
                              │ Fibonacci
            gem:fibonacci-evs │ Version: 0.1.2
                              │ http://github.com/edsimpson/fibonacci-evs
                              │ Test gem with a Fibonacci-related method for
                              │ Fixnum and Bignum.
         gem:simple_fibonacci │ Version: 0.1.2
                              │ http://github.com/anjshenoy/simple_fibonacci
                              │ Gem that calculates fibonacci numbers upto a
                              │ a provided number
──────────────────────────────┴─────────────────────────────────────────────────

$ aero info gem:fibonacci

────────────────────────────────────────────────────────────────────────────────
                 INFORMATION:   fibonacci
──────────────────────────────┬─────────────────────────────────────────────────
                     authors: │ Chaitanya Vellanki
                      bindir: │ bin
                        date: │ 2012-11-09
                 description: │ A Ruby gem for exploring Fibonacci series
                       email: │ me@chaitanyavellanki.com
                    has_rdoc: │ True
                    homepage: │ http://github.com/chaitanyav/fibonacci
                        name: │ fibonacci
                    platform: │ ruby
               require_paths: │ lib
       required_ruby_version: │ >= 0
   required_rubygems_version: │ >= 0
           rubyforge_project: │ fibonacci
            rubygems_version: │ 1.3.6
       specification_version: │ 3
                     summary: │ Fibonacci
                     version: │ 0.1.7
──────────────────────────────┴─────────────────────────────────────────────────

```

Special notes:

Search is executed with the ``-qbd`` arguments which will return both locally installed and remotely available packages.
Info is obtained through the ``specification`` command which returns a gemspec class tagged YAML document, nuff said.

Npm
---
Supported commands:

* search
* install
* info

```
    $ aero search npm:fibonacci-async

                                        PACKAGE NAME   DESCRIPTION
            ________________________________________   __________________________________________________
                                 npm:fibonacci-async : 2012-10-29 22:03
                                                       So, you want to benchmark node.js with fibonacci
                                                       once again? - Here's the library for that. You're
                                                       welcome.

    $ aero info npm:fibonacci-async

                                                       INFORMATION: fibonacci-async
           ________________________________________    __________________________________________________
                                            author: :  Enno Boland <eb@s01.de>
                                       description: :  So, you want to benchmark node.js with fibonacci
                                                       once again? - Here"s the library for that. You"re
                                                       welcome.
                                              dist: :  tarball: http://registry.npmjs.org/fibonacci-async
                                                       /-/fibonacci-async-0.0.2.tgz
                                                       shasum: 173d4d28b038723f41bacc660edc331b1e526047
                                         dist-tags: :  latest: 0.0.2
                                           engines: :  node: *
                                              main: :  lib/binding.js
                                       maintainers: :  Gottox <g@s01.de>
                                              name: :  fibonacci-async
                                        repository: :  url: git://github.com/Gottox/fibonacci-async.git
                                                       type: git
                                           scripts: :  preinstall: node-waf clean || (exit 0); node-waf
                                                       configure build
                                              time: :  0.0.1: 2012-05-26T11:24:06.960Z
                                                       0.0.2: 2012-05-26T11:25:45.254Z
                                           version: :  0.0.2
                                          versions: :  0.0.1, 0.0.2

```

Special notes:

Info uses the ``npm view`` command which return a JavaScript object of the registry which we then nudge closer to resembling JSON format so that we may proceed to parse it with **:mod:json**

Pear
----
Supported commands:

* search
* install
* info

```
    $ aero search pear:fibonacci

                                        PACKAGE NAME   DESCRIPTION
            ________________________________________   __________________________________________________
                                 pear:Math_Fibonacci : Version:0.8 (stable)
                                                       http://pear.php.net/Math_Fibonacci
                                                       Package to calculate and manipulate Fibonacci
                                                       numbers

    $ aero info pear:Math_Fibonacci

                                                       INFORMATION:
           ________________________________________    __________________________________________________
                                            Latest: :  0.8
                                         Installed: :  - no -
                                           Package: :  Math_Fibonacci
                                           License: :  PHP
                                          Category: :  Math
                                           Summary: :  Package to calculate and manipulate Fibonacci
                                                       numbers
                                       Description: :  The Fibonacci series is constructed using the
                                                       formula:
                                                       F(n) = F(n - 1) + F (n - 2),
                                                       By convention F(0) = 0, and F(1) = 1.
                                                       An alternative formula that uses the Golden
                                                       Ratio can also be used:
                                                       F(n) = (PHI^n - phi^n)/sqrt(5) [Lucas'
                                                       formula],
                                                       where PHI = (1 + sqrt(5))/2 is the Golden Ratio,
                                                       and
                                                       phi = (1 - sqrt(5))/2 is its reciprocal
                                                       Requires Math_Integer, and can be used with big
                                                       integers if the GMP or
                                                       the BCMATH libraries are present.

```

Pear
----
Supported commands:

* search
* install
* info

```
    $ aero search pecl:ncurses

                                        PACKAGE NAME   DESCRIPTION
            ________________________________________   __________________________________________________
                                        pecl:ncurses : Version:1.0.2 (stable)
                                                       http://pecl.php.net/ncurses
                                                       Terminal screen handling and optimization package

    $ aero info pecl:ncurses

                                                       INFORMATION: ncurses
           ________________________________________    __________________________________________________
                                            Latest: :  1.0.2
                                         Installed: :  - no -
                                           Package: :  ncurses
                                           License: :  PHP
                                          Category: :  Console
                                           Summary: :  Terminal screen handling and optimization
                                                       package
                                       Description: :  ncurses (new curses) is a free software
                                                       emulation of curses in
                                                       System V Rel 4.0 (and above). It uses terminfo
                                                       format, supports
                                                       pads, colors, multiple highlights, form
                                                       characters and function
                                                       key mapping. Because of the interactive nature
                                                       of this library,
                                                       it will be of little use for writing Web
                                                       applications, but may
                                                       be useful when writing scripts meant using PHP
                                                       from the command
                                                       line.
                                                       See also
                                                       http://www.gnu.org/software/ncurses/ncurses.html

Pip
---
Supported commands:

* search
* install
* info

```
    $ aero search pip:ncurses

                                        PACKAGE NAME   DESCRIPTION
            ________________________________________   __________________________________________________
                                           pip:Canto : Version: 0.7.10         Score: 110
                                                       An ncurses RSS aggregator.
                                         pip:chronos : Version: 0.2            Score:  13
                                                       An ncurses stopwatch/timer.
                                    pip:gocept.httop : Version: 1.0            Score:   1
                                                       An ncurses-based tool to monitor website
                                                       responsiveness in real-time.

    $ aero info pip:Canto

                                                       INFORMATION: Canto
           ________________________________________    __________________________________________________
                                  Metadata-Version: :  1.0
                                              Name: :  Canto
                                           Version: :  0.7.10
                                           Summary: :  An ncurses RSS aggregator.
                                         Home-page: :  http://codezen.org/canto
                                            Author: :  Jack Miller
                                      Author-email: :  jack@codezen.org
                                           License: :  GPLv2
                                      Download-URL: :  http://codezen.org/static/canto-0.7.10.tar.gz
                                       Description: :  UNKNOWN
                                          Platform: :  linux

```
Special notes:

The Pip adaptor does not use subprocess to execute pip command line interface but instead we use the pip library directly. This strategy now enables us to get pip info, functionality that is not exposed on the CLI but very much available as you can see, marking a huge advance for aero.

```
Pyrus
----
Supported commands:

* search
* install
* info

```
    $ aero search pyrus:ncurses


                                        PACKAGE NAME   DESCRIPTION
            ________________________________________   __________________________________________________
                          pyrus:pecl.php.net/ncurses : Version: 1.0.2 (API 1.0.0)
                                                       http://pecl.php.net/ncurses
                                                       Terminal screen handling and optimization package

    $ aero info pyrus:pecl.php.net/ncurses

                                                       INFORMATION: pecl.php.net/ncurses
           ________________________________________    __________________________________________________
                                           Version: :  1.0.2 (API 1.0.0)
                                         Stability: :  stable (API stable)
                                      Release Date: :  2012-06-16 17:05:19
                                           Summary: :  Terminal screen handling and optimization package
                                       Description: :  ncurses (new curses) is a free software emulation
                                                       of curses in System V Rel 4.0 (and above). It uses
                                                       terminfo format, supports pads, colors, multiple
                                                       highlights, form ch...
                                     Release Notes: :  - Fixed build on PHP 5.3+ - Fixed bug #60853
                                                       (Missing NCURSES_KEY_HOME constant)...


```
Special notes:

Similar to brew, with pyrus you are also required to call info should you require more details about a particular package. Luckily aero is more considerate and will call info on your behalf to provide you with more information in the search results.


Macports
--------
Supported commands:

* search
* install
* info

```
    $ aero search port:cowsay

                                        PACKAGE NAME   DESCRIPTION
            ________________________________________   __________________________________________________
                                         port:cowsay : @3.03 (textproc, amusements, games) Configurable
                                                       talking characters in ASCII art
                                          port:insub : @13.0 (irc) extra cowsay cows and irssi script

    $ aero info port:insub

                                                       INFORMATION: insub
           ________________________________________    __________________________________________________
                                           Version: :  @13.0 (irc)
                                       Description: :  Handy tools for being obnoxious on IRC. Warning:
                                                       some of the cows are potentially offensive.
                                          Homepage: :  http://gruntle.org/projects/irssi/insub/
                                         Platforms: :  darwin
                                           License: :  unknown
                                       Maintainers: :  nomaintainer@macports.org

```

Going forward
-------------

As well as extending the current functionality we also plan to support:

* fink
* apt-get
* composer local

Known issues
------------

Items that require some attention: (Let us know if you want to tackle any of these)

* The pass through is dodgy, some issues with argparse, passing --long-name-args in quotes work but -l short name fails.
* Autocomplete should complete known packages obtained through searching.
* No unit tests as yet
* Limited to no codedocs

Changelog
---------
 * v0.0.1 alpha 2
   * Pip info capable now - whoop whoop!
   * Fixed unicode issues
   * Pip via pip library instead of sub-process
   * Improved adapter implementation
   * Improved resources free on exit
   * Improved pass through implementation
   * Improved output display and fix typos
   * Updated documentation

 * v0.0.1 alpha 1 - 2012-12-02
  * Fixed installation issues and dependency installation
  * Increased cache granularity command:adapter:package
  * Support for multiple packages simultaneously
  * Support for pass through arguments
  * Progress indication
  * Major BaseCommand refactor and Piped Coroutine workflow
  * BaseAdapter refactor to simplify adapter implementations
  * Colorized output goodness
  * Tap brew extended repositories
  * Optimize screen real estate utilization - display Version, url (where available) and Short description only in search results
  * In process piped output - pager without a tmp file
  * DebugCommand support to simplify adapter creation
  * Added support for pear, pecl, pyrus
  * Gracefully accept abnormal program termination
  * Search commands that require more info now uses aero which caches the info details for each package

License
-------

The New BSD License. see LICENSE.txt

Acknowledge
-----------

Original Ascii art done by:

* Si Deane
* Chad Vice
* Scott Davey
* Wil Dixon
* Brad Leftwich
* Thor Aage Eldby
* Ennis Trimble
* Joan Stark
* Jochem Berends


                                           __/\__
                                          `==/\==´
         _         _____        ____________/__\____________        _____         _
        (__\______o=/ /=_ |    /____________________________\    | _=\ \=o______/__)
        >---\\\\ _/_/_^^]:>      __||__||__/.--.\__||__||__      <:[^^_\_\_ ////---<
        __       _/_/|´´  |     /__|___|___( >< )___|___|__\     |  ``|\_\_       __
        | \_________<0)____________________0`--´0____________________(0>_________/ |
        |                                                                          |
        |                    Brought to you by the Respect team.                   |
        |__________________________________________________________________________|

