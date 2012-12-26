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
         O  \                                 aero v0.0.1 alpha 2
    ─────────\────────────────────────────────────────────────────────
              \
               \

Platform
--------

Written in python using v 2.7, this may or may not be the entry requirement for now, on Mac OS X currently and the excellent IDE `PyCharm by JetBrains <http://www.jetbrains.com/pycharm/>`_ which you may consider highly recommended do give it a try. The \*nixes will likely be included soon, there exists no bias to the MS platforms only less accessible as a product of choice and opportunity I guess. Feel free to suggest other usages or specific requirements you might have.

After some serious deliberations even though the majority of the team has zero to no python experience at all it will never the less prevent us, like the good professional programmers we are, from using the best hammer for hitting the particular nails or fingers. This has been an interesting learning curve so far and I have to agree python is a pleasure and does suite the requirements like a glove and now that we are empowered with some new lingo like "pythonic" and "tupels" not to mention "generators" and the other "PEP" "recipes" of convenience we make no claim that this is an exemplary python implementation but we sure as the indents are important will try. Feel free to pin-point any obvious mistakes by raising an issue so we may apologise or be damned to continue in err without permission as we continue under assumption that this is the pythonic way. Now I guess I should go read the book perhaps =)


Disclaimer
----------

Even though using **aero** can cause you or your system no harm, by design and while we are using it everyday for a one stop interface to finding the software we need to install we need to warn you about two things:

1. This is still a work in progress and you are welcome to pitch in, lend a hand, test, report bugs, request features or make a donation but keep in mind that you will find unfinished and more than likely some broken things.
2. May lead to compulsive package installation disorders can cause dependency and some serious addictions, use at your own risk.

Installation
------------

+ aero install with pip (egg and chicken)

aero installation if you already have aero - from version 0.0.1a1 pip will always reinstall::

    $ aero install pip:https://github.com/Aeronautics/aero/tarball/develop

aero install with pip --upgrade - upgrade aero and dependencies  - from version 0.0.1a1::

    $ aero install pip:https://github.com/Aeronautics/aero/tarball/develop --- "--upgrade"

+ pip installation

aero can be installed directly from github via pip with the following command::

    $ pip install --upgrade https://github.com/Aeronautics/aero/tarball/develop

+ through easy_install

if you prefer using easy_install the following command will download and install aero from github::

    $ easy_install https://github.com/Aeronautics/aero/tarball/develop

+ From git repository

Clone the repo from github or fork it first and then clone your copy if you want to help out with pull requests. Then just run the setup.py with install::

    $ ./setup.py install


Running aero
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

       ┌────────────────────┐
    ┌──┘ Usage Instructions └───────────────────────────────────────────────────┐
    └───────────────────────────────────────────────────────────────────────────┘

     aero.py [-h] [-v] [-p PAGER] [-d [{npm,pyrus,pear,pip,brew,pecl,gem}]]
                   [-i] [--- PASSTHRU]
                   command [mngr:]package ...

       ┌──────────────────┐
    ┌──┘ Argument Options └─────────────────────────────────────────────────────┐
    └───────────────────────────────────────────────────────────────────────────┘

    optional arguments:
      -h, --help            show this help message and exit
      -v, --version         Show program's version number and exit
      -p, --pager PAGER     The pager to use for long paged displays. The default
                            is based on the environment variable $PAGER, if it is
                            not set, some common pagers like 'less', 'more',
                            'most' and finally 'cat' are tried, in this order.

                            default: None

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


       ┌────────────────┐
    ┌──┘ Commands Usage └───────────────────────────────────────────────────────┐
    └───────────────────────────────────────────────────────────────────────────┘

    Command arguments:

      The aero commands are based on the typical package manager
      commands followed by the package name(s) to perform the task on.
      At least one command is required but several packages can be
      processed simultaneously.
      Use 'aero command --help' to get further details for specific
      commands.

      command [mngr:]package
                            Optionally provide the specific manager to use
                            prepended to the package name(s) with a colon ':' or
                            alternatively aero will execute the command against
                            all enabled package managers.

        choose one of the following valid aero commands:

        search              Do an aero search for packages
        install             Do an aero install package(s)
        info                Do an aero info for packages

    Configuration argument:
      command [mngr:]package
                            Optionally provide the specific manager to use
                            prepended to the package name(s) with a colon ':' or
                            alternatively aero will execute the command against
                            all enabled package managers.

        choose one of the following valid aero commands:

        search              Do an aero search for packages
        install             Do an aero install package(s)
        info                Do an aero info for packages

    Configuration argument:

      It is possible to load aero configuration from an input file.

      @filename             Append "key, value" (where applicable) to a file one
                            argument, value pair per line. To tell aero which
                            file to use for configuration specify the path and
                            file name prefixed with an "@".


Commands
--------

With **aero** you can expect to use the common commands and we will translate them to the package manager specific instructions where they may have chosen to deviate from the norm. Currently the following commands are implemented:

Usage::

    $ aero <command> <packages...>

Where packages are one or more package names optionally prefixed with the specific package manager, colon separated. The ``mngr:package`` format produced in search is used to instruct a specific package manager with any commands. Omitting the prefix instruction will result in all active package managers being instructed to complete the task. This may or may not necessarily have the desired effect. Multiple packages from different package managers can all be processed with one aero command.

* search

To search for a package which will produce a list with the package manager prefixed the package name by ``\:`` and a short description of the package.

* install

To instruct the installation of a given package.

* info

To obtain more detailed information regarding a given package now also available for pip.


Package managers
================

The following package managers have been recycled, more will follow. Let us know if your favourite packaging tool is missing or submit a pull request with  new adapter you'd like added.

﻿Advanced Package Tool
---------------------
Supported commands:

* search
* install
* info

::

    $ aero search apt:fibonacci

    ﻿────────────────────────────────────────────────────────────────────────────────
                     PACKAGE NAME   DESCRIPTION
    ──────────────────────────────┬─────────────────────────────────────────────────
       apt:libmath-fibonacci-perl │ Fibonacci numbers calculations Perl module
                apt:python-pqueue │ a priority queue extension for Python
                    apt:qtstalker │ commodity and stock market charting and
                                  │ technical analysis
    ──────────────────────────────┴─────────────────────────────────────────────────

    $ aero info apt:libmath-fibonacci-perl

    ﻿────────────────────────────────────────────────────────────────────────────────
                     INFORMATION:   libmath-fibonacci-perl
    ──────────────────────────────┬─────────────────────────────────────────────────
                         Package: │ libmath-fibonacci-perl
                        Priority: │ optional
                         Section: │ universe/perl
                  Installed-Size: │ 64
                      Maintainer: │ Ubuntu MOTU Developers <ubuntu-
                                  │ motu@lists.ubuntu.com>
             Original-Maintainer: │ Debian Perl Group <pkg-perl-
                                  │ maintainers@lists.alioth.debian.org>
                    Architecture: │ all
                         Version: │ 1.5-4
                         Depends: │ perl (>= 5.6.0-16)
                        Filename: │ pool/universe/libm/libmath-fibonacci-perl
                                  │ /libmath-fibonacci-perl_1.5-4_all.deb
                            Size: │ 6902
                          Md5Sum: │ 7be8cecc5fcd6c44d02a19dce5930396
                            Sha1: │ d6936f3710cf7d995cd9f2e925ee6f6e912a3327
                          Sha256: │ 194a2f8c11dd492074745633c52f07392b537580f015a8
                                  │ 1bd20e9ca31c99cabd
    ﻿              Description-En: │ Fibonacci numbers calculations Perl module
                                  │ This module provides a few functions related
                                  │ to Fibonacci numbers,  such as getting the n
                                  │ term of a Fibonacci sequence, compute and
                                  │ return the first n Fibonacci numbers,
                                  │ decompose an integer into the  sum of
                                  │ Fibonacci numbers, etc.
                        Homepage: │ http://search.cpan.org/dist/Math-Fibonacci/
                 Description-Md5: │ 11f9aaf15742de4ebb30a58b77eabee3
                            Bugs: │ https://bugs.launchpad.net/ubuntu/+filebug
                          Origin: │ Ubuntu
    ──────────────────────────────┴─────────────────────────────────────────────────


Homebrew
--------
Supported commands:

* search
* install
* info

::

    $ aero search brew:ncurses

    ────────────────────────────────────────────────────────────────────────────────
                     PACKAGE NAME   DESCRIPTION
    ──────────────────────────────┬─────────────────────────────────────────────────
                     brew:ncurses │ Version:stable 5.9
                                  │ http://www.gnu.org/s/ncurses/
                                  │ /usr/local/Cellar/ncurses/5.9 (1777 files,
    ──────────────────────────────┴─────────────────────────────────────────────────

    $ aero info brew:ncurses

    ────────────────────────────────────────────────────────────────────────────────
                     INFORMATION:   ncurses
    ──────────────────────────────┬─────────────────────────────────────────────────
                         Version: │ stable 5.9
                                  │ http://www.gnu.org/s/ncurses/
                                  │ /usr/local/Cellar/ncurses/5.9 (1777 files,
                                  │ 18M) *
                                  │ ==> Options
                                  │ --universal
                                  │ Build a universal binary
    ──────────────────────────────┴─────────────────────────────────────────────────


Special notes:

Brew has the inclination to only return the package names on search, in addition to retrieval of the package names aero continues to further query info on each package from where it is able to parse and present slightly more usable information. Instead of just calling the info command on the package manager we execute `aero info` instead which means that all the information for every package listed in the search results is already cached and retrievable instantaneously.

Gem
---
Supported commands:

* search
* install
* info

::

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
                                  │ http://github.com/beckram23/closest-fibonacci-
                                  │ gem
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
                                  │ Gem that calculates fibonacci numbers upto a a
                                  │ provided number
    ──────────────────────────────┴─────────────────────────────────────────────────

    $ aero info gem:fibonacci

    ────────────────────────────────────────────────────────────────────────────────
                     INFORMATION:   fibonacci
    ──────────────────────────────┬─────────────────────────────────────────────────
                         Authors: │ Chaitanya Vellanki
                          Bindir: │ bin
                            Date: │ 2012-11-09
                     Description: │ A Ruby gem for exploring Fibonacci series
                           Email: │ me@chaitanyavellanki.com
                        Has_Rdoc: │ True
                        Homepage: │ http://github.com/chaitanyav/fibonacci
                            Name: │ fibonacci
                        Platform: │ ruby
                   Require_Paths: │ lib
           Required_Ruby_Version: │ >= 0
       Required_Rubygems_Version: │ >= 0
               Rubyforge_Project: │ fibonacci
                Rubygems_Version: │ 1.3.6
           Specification_Version: │ 3
                         Summary: │ Fibonacci
                         Version: │ 0.1.7
    ──────────────────────────────┴─────────────────────────────────────────────────


Special notes:

Search is executed with the ``-qbd`` arguments which will return both locally installed and remotely available packages.
Info is obtained through the ``specification`` command which returns a gemspec class tagged YAML document, nuff said.

Npm
---
Supported commands:

* search
* install
* info

::

    $ aero search npm:fibonacci-async

    ────────────────────────────────────────────────────────────────────────────────
                     PACKAGE NAME   DESCRIPTION
    ──────────────────────────────┬─────────────────────────────────────────────────
              npm:fibonacci-async │ 2012-10-29 22:03
                                  │ So, you want to benchmark node.js with
                                  │ fibonacci once again? - Here's the library for
                                  │ that. You're welcome.
    ──────────────────────────────┴─────────────────────────────────────────────────

    $ aero info npm:fibonacci-async

    ────────────────────────────────────────────────────────────────────────────────
                     INFORMATION:   fibonacci-async
    ──────────────────────────────┬─────────────────────────────────────────────────
                          Author: │ Enno Boland <eb@s01.de>
                     Description: │ So, you want to benchmark node.js with
                                  │ fibonacci once again? - Here"s the library for
                                  │ that. You"re welcome.
                            Dist: │ tarball: http://registry.npmjs.org/fibonacci-
                                  │ async/-/fibonacci-async-0.0.2.tgz
                                  │ shasum:
                                  │ 173d4d28b038723f41bacc660edc331b1e526047
                       Dist-Tags: │ latest: 0.0.2
                         Engines: │ node: *
                            Main: │ lib/binding.js
                     Maintainers: │ Gottox <g@s01.de>
                            Name: │ fibonacci-async
                      Repository: │ url: git://github.com/Gottox/fibonacci-
                                  │ async.git
                                  │ type: git
                         Scripts: │ preinstall: node-waf clean || (exit 0); node-
                                  │ waf configure build
                            Time: │ 0.0.1: 2012-05-26T11:24:06.960Z
                                  │ 0.0.2: 2012-05-26T11:25:45.254Z
                         Version: │ 0.0.2
                        Versions: │ 0.0.1, 0.0.2
    ──────────────────────────────┴─────────────────────────────────────────────────

Special notes:

Info uses the ``npm view`` command which return a JavaScript object of the registry which we then nudge closer to resembling JSON format so that we may proceed to parse it with **:mod:json**

Pear
----
Supported commands:

* search
* install
* info

::

    $ aero search pear:fibonacci

    ────────────────────────────────────────────────────────────────────────────────
                     PACKAGE NAME   DESCRIPTION
    ──────────────────────────────┬─────────────────────────────────────────────────
              pear:Math_Fibonacci │ Version:0.8 (stable)
                                  │ http://pear.php.net/Math_Fibonacci
                                  │ Package to calculate and manipulate Fibonacci
                                  │ numbers
    ──────────────────────────────┴─────────────────────────────────────────────────

    $ aero info pear:Math_Fibonacci

    ────────────────────────────────────────────────────────────────────────────────
                     INFORMATION:   Math_Fibonacci
    ──────────────────────────────┬─────────────────────────────────────────────────
                          Latest: │ 0.8
                       Installed: │ - no -
                         Package: │ Math_Fibonacci
                         License: │ PHP
                        Category: │ Math
                         Summary: │ Package to calculate and manipulate Fibonacci
                                  │ numbers
                     Description: │ The Fibonacci series is constructed using the
                                  │ formula: F(n) = F(n - 1) + F (n - 2), By
                                  │ convention F(0) = 0, and F(1) = 1. An
                                  │ alternative formula that uses the Golden Ratio
                                  │ can also be used: F(n) = (PHI^n -
                                  │ phi^n)/sqrt(5) [Lucas' formula], where PHI =
                                  │ (1 + sqrt(5))/2 is the Golden Ratio, and phi =
                                  │ (1 - sqrt(5))/2 is its reciprocal Requires
                                  │ Math_Integer, and can be used with big
                                  │ integers if the GMP or the BCMATH libraries
                                  │ are present.
    ──────────────────────────────┴─────────────────────────────────────────────────


Pear
----
Supported commands:

* search
* install
* info

::

    $ aero search pecl:ncurses

    ────────────────────────────────────────────────────────────────────────────────
                     PACKAGE NAME   DESCRIPTION
    ──────────────────────────────┬─────────────────────────────────────────────────
                     pecl:ncurses │ Version:1.0.2 (stable)
                                  │ http://pecl.php.net/ncurses
                                  │ Terminal screen handling and optimization
                                  │ package
    ──────────────────────────────┴─────────────────────────────────────────────────

    $ aero info pecl:ncurses

    ────────────────────────────────────────────────────────────────────────────────
                     INFORMATION:   ncurses
    ──────────────────────────────┬─────────────────────────────────────────────────
                          Latest: │ 1.0.2
                       Installed: │ - no -
                         Package: │ ncurses
                         License: │ PHP
                        Category: │ Console
                         Summary: │ Terminal screen handling and optimization
                                  │ package
                     Description: │ ncurses (new curses) is a free software
                                  │ emulation of curses in System V Rel 4.0 (and
                                  │ above). It uses terminfo format, supports
                                  │ pads, colors, multiple highlights, form
                                  │ characters and function key mapping. Because
                                  │ of the interactive nature of this library, it
                                  │ will be of little use for writing Web
                                  │ applications, but may be useful when writing
                                  │ scripts meant using PHP from the command line.
                                  │ See also http://www.gnu.org/software/ncurses/n
                                  │ curses.html
    ──────────────────────────────┴─────────────────────────────────────────────────


Pip
---
Supported commands:

* search
* install
* info

::

    $ aero search pip:ncurses

    ────────────────────────────────────────────────────────────────────────────────
                     PACKAGE NAME   DESCRIPTION
    ──────────────────────────────┬─────────────────────────────────────────────────
                        pip:Canto │ Version: 0.7.10       Score: 110
                                  │ An ncurses RSS aggregator.
                      pip:chronos │ Version: 0.2          Score:  13
                                  │ An ncurses stopwatch/timer.
                 pip:gocept.httop │ Version: 1.0          Score:   1
                                  │ An ncurses-based tool to monitor website
                                  │ responsiveness in real-time.
    ──────────────────────────────┴─────────────────────────────────────────────────

    $ aero info pip:Canto

    ────────────────────────────────────────────────────────────────────────────────
                     INFORMATION:   Canto
    ──────────────────────────────┬─────────────────────────────────────────────────
                Metadata-Version: │ 1.0
                            Name: │ Canto
                         Version: │ 0.7.10
                         Summary: │ An ncurses RSS aggregator.
                       Home-Page: │ http://codezen.org/canto
                          Author: │ Jack Miller
                    Author-Email: │ jack@codezen.org
                         License: │ GPLv2
                    Download-Url: │ http://codezen.org/static/canto-0.7.10.tar.gz
                     Description: │ UNKNOWN
                        Platform: │ linux
    ──────────────────────────────┴─────────────────────────────────────────────────

Special notes:

The Pip adaptor does not use subprocess to execute pip command line interface but instead we use the pip library directly. This strategy now enables us to get pip info, functionality that is not exposed on the CLI but very much available as you can see, marking a huge advance for aero.

Pyrus
-----
Supported commands:

* search
* install
* info

::

    $ aero search pyrus:ncurses

    ────────────────────────────────────────────────────────────────────────────────
                     PACKAGE NAME   DESCRIPTION
    ──────────────────────────────┬─────────────────────────────────────────────────
       pyrus:pecl.php.net/ncurses │ Version:1.0.2 (API 1.0.0)
                                  │ http://pecl.php.net/ncurses
                                  │ Terminal screen handling and optimization
                                  │ package
    ──────────────────────────────┴─────────────────────────────────────────────────

    $ aero info pyrus:pecl.php.net/ncurses

    ────────────────────────────────────────────────────────────────────────────────
                     INFORMATION:   pecl.php.net/ncurses
    ──────────────────────────────┬─────────────────────────────────────────────────
                         Version: │ 1.0.2 (API 1.0.0)
                       Stability: │ stable (API stable)
                    Release Date: │ 2012-06-16 17:05:19
                         Summary: │ Terminal screen handling and optimization
                                  │ package
                     Description: │ ncurses (new curses) is a free software
                                  │ emulation of curses in System V Rel 4.0 (and
                                  │ above). It uses terminfo format, supports
                                  │ pads, colors, multiple highlights, form ch...
                   Release Notes: │ - Fixed build on PHP 5.3+ - Fixed bug #60853
                                  │ (Missing NCURSES_KEY_HOME constant)...
    ──────────────────────────────┴─────────────────────────────────────────────────

Special notes:

Similar to brew, with pyrus you are also required to call info should you require more details about a particular package. Luckily aero is more considerate and will call info on your behalf to provide you with more information in the search results.


Macports
--------
Supported commands:

* search
* install
* info

::

    $ aero search port:cowsay

    ────────────────────────────────────────────────────────────────────────────────
                     PACKAGE NAME   DESCRIPTION
    ──────────────────────────────┬─────────────────────────────────────────────────
                      port:cowsay │ @3.03 (textproc, amusements, games) Configurable
                                  │ talking characters in ASCII art
                      port:insub  │ @13.0 (irc) extra cowsay cows and irssi script
    ──────────────────────────────┴─────────────────────────────────────────────────

    $ aero info port:insub

    ────────────────────────────────────────────────────────────────────────────────
                     INFORMATION:   insub
    ──────────────────────────────┬─────────────────────────────────────────────────
                Metadata-Version: │ 1.0
                         Version: │ @13.0 (irc)
                     Description: │ Handy tools for being obnoxious on IRC. Warning:
                                  │ some of the cows are potentially offensive.
                        Homepage: │ http://gruntle.org/projects/irssi/insub/
                       Platforms: │ darwin
                         License: │ unknown
                     Maintainers: │ nomaintainer@macports.org
    ──────────────────────────────┴─────────────────────────────────────────────────


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
    * Pip via pip library instead of sub-process
    * Unicode done right
    * Use unicode box drawing chars in output
    * Normalized info output title case
    * Refactored commands as package
    * Refactored arguments
    * Improved command line argument exposure
    * RF CommandProcessor render method extraction
    * Improved pager detection (lazy)
    * Replaced autocompletion with argcomplete
    * Improved imports (lazy)
    * Improved adapter implementation
    * Improved resources free on exit
    * Improved pass through implementation
    * Improved output display and fix typos
    * Improved output for pecl and pear
    * Repaired pyrus adapter
    * Added support for Advanced Package Manage (apt)
    * Tested on Linux (ubuntu)
    * Terminal window actual size consideration, works with 80 cols or more
    * Get dependencies from requirements.txt
    * Pygmentized help output
    * Using codecs.open instead of file.open for assets
    * Documentation as Restructured Text (rst)
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

::

                                       __/\__
                                      `==/\==´
     _         _____        ____________/__\____________        _____         _
    (__\______o=/ /=_ |    /____________________________\    | _=\ \=o______/__)
    >---\\\\ _/_/_^^]:>      __||__||__/.--.\__||__||__      <:[^^_\_\_ ////---<
    __       _/_/|´´  |     /__|___|___( >< )___|___|__\     |  ``|\_\_       __
    │ \_________<0)____________________0`--´0____________________(0>_________/ │
    │                                                                          │
    │                    Brought to you by the Respect team.                   │
    └──────────────────────────────────────────────────────────────────────────┘
