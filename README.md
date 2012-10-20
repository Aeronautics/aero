====
aero
====

The **aero** command line package recycler. It uses package managers you already have.

Instead of having to consult several package managers when you are looking for something you can now search through all of them using the same commands and find similar results using the same tool.

When you type ``aero search php``, **aero** already knows which package managers are installed and starts collecting information from each package manager while caching the results for when you havent found exactly what you're looking for yet. Other advanced features besides caching includes intutive help and command line arguments parsing, loading configurations from file, bash and zsh autocompletion, results paging so that you don't have to always scroll up when the information you nood is right at the top of the results that just came flying by but you also wont get dumped into a pager, of your choice I should add, if the results would fit on a single page and doesn't require paging. These are just some of the features already incorporated to enhance your user experience setting new standards for enjoyable software management.

Even though **aero** is some serious machining it will only focus on the task its set out to do, to recycle your existing package managers and you can rest assured/or continue to worry whichever might be the case, as **aero** will leave the heavy lifting upto the software partners already tasked with the use case requirements and instead only focuses on the end user requirements through consistent interfaces, intuitive interactions and all the information you require at your fingertips enabling you to make the decisions you need to accomplish the tasks at hand.::

  
     \
      \
       \ \    .           _____    ___________  ____
        \_\__/            \__  \ _/ __ \_  __ \/  _ \
       O__| \ \            / __ \\  ___/|  | \(  <_> )
          \ o\/           (____  /\___  >__|   \____/
           \_/\                \/     \/
           / \ \
           O  \                                          aero v0.0.1 alpha 0
      _________\_____________________________________________________
                \
                
              
Platform
--------

Written in python using v 2.7, this may or may not be the entry requirement for now, on Mac OS X currently and the excellent IDE [PyCharm by JetBrains](http://www.jetbrains.com/pycharm/) which you may consider highly reccommended do give it a try. The *nixes will likely be included soon, there exists no bias to the MS platforms only less accessible as a product of choice and opportunity I guess. Feel free to suggest other usages or specific requirements you might have. 

After some serious deliberations even though the majority of the team has zero to no python experience at all it will never the less prevent us, like the good professional programmers we are, from using the best hammer for hitting the particular nails or fingers. This has been an interesting learning curve so far and I have to agree python is a pleasure and does suite the requirements like a glove and now that we are empowered with some new lingo like "pythonic" and "tupels" not to mention "generators" and the other "PEP" "recipes" of convenience we make no claim that this is an exemplary python implementation but we sure as the indents are important will try. Feel free to pin-point any obvious mistakes by raising an issue so we may appologise or be damned to continue in err without permission as we continue under assumption that this is the pythonic way. Now I guess I should go read the book perhaps =)


Disclaimer
----------

Even though using **aero** can cause you or your system no harm, by design and while we are using it everyday for a one stop interface to finding the software we need to install we need to warn you about two things:

1. This is still a work in progress and you are welcome to pitch in, lend a hand, test, report bugs, request features but keep in mind that you will find unfinished and more than likely some broken things.
2. May lead to some serious impulse package installation addictions, use at your own risk.

Installation
------------

Ideally it would be installable you would imagine and some lengths have been taken to wrap it as a package and provide the setup.py stubs et al but alas at the time of this writing this does not succeed as yet.

Success! We can install and it appears dependencies are also being discovered correctly, the question now is does it work for you too.

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

Running the aero.py executable from the root package folder also works and may be simlinked in your path if you need another approach while we iron out the kinks.

Running aero:
------------
On execution of **aero** with no requirements a short usage instruction will be presented::

    $ aero
    
    aero v0.0.1 alpha 0
    
    usage: myaero [-h] [-v] [-p PAGER] [-d [{Brew,Port,Pip,Npm,Gem,Colour}]] [-i]
                  [-c {bash,zsh}]
                  command [mngr:] package ...
    myaero: error: too few arguments

Providing **aero** with the customary ``--help`` argument will give more detailed information::

    $ aero
    
        ____________________
     __/ Usage Instructions \___________________________________________________
    |___________________________________________________________________________|
    
     myaero [-h] [-v] [-p PAGER] [-d [{Brew,Port,Pip,Npm,Gem,Colour}]] [-i]
                  [-c {bash,zsh}]
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
                            
      -d, --disable [{Brew,Port,Pip,Npm,Gem,Colour}]
    
                            Add the items you wish to disable to the list.
                            Multiple disable arguments may be supplied. 
                            
                            default: []
                            
      -i, --invalidate-cache 
                            Clear the search cache and enquire anew from the
                            package managers. 
                            
                            default: False
                            
      -c, --completion {bash,zsh}
                            Command outo completion is supported for both bash and
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
      commands followed by the package name to perform the task on.
      Use "aero cammand --help" to get further details for specific
      commands.
    
      command [mngr:]package
                            Optionally provide the specific manager to use
                            prepended to the package name with a colon ":" or
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

With **aero** you can expect to use the common commands and we will translate them to the package manager specific instructions where they may have chosen to deviate from the norm. Currently the following commands are implimented:

* search  
To seach for a packoge which will produce a list with the package manager prefixed the package name by ":" and a short description of the packoge.
* install  
To instruct the installation of a given package. The ``mngr:package`` format produced in search is used to instruct a specific package manager with any commands. Omitting the instruction will result in all active package managers being instructed. This may or may not necessarily have the desired effect.
* info  
To obtain more detailed information regarding a given packoge where available.

Package managers
================

The following package managers has been enabled, more will follow:

Hombrew
-------
Supported commands:

* search
* install
* info

```
    $ aero search brew:cowsay
    
                                        PACKAGE NAME   DESCRIPTION
            ________________________________________   __________________________________________________
                                         brew:cowsay : version: stable 3.03
                                                       http://www.nog.net/~tony/warez/cowsay.shtml
                                                       /usr/local/Cellar/cowsay/3.03 (53 files, 228K) *


    $ aero info brew:cowsay

                                                       INFORMATION: cowsay
            ________________________________________   __________________________________________________
                                             version : stable 3.03
                                                       http://www.nog.net/~tony/warez/cowsay.shtml
                                                       /usr/local/Cellar/cowsay/3.03 (53 files, 228K) *

```

Special notes:

Brew has the inlination to only return the package names on search, in addition to retrieval of the packoge names aero continues to further query info on each package from where it is able to parse and present slightly  more information.        

Gem
---
Supported commands:

* search
* install

```
    $ aero search gem:fibonacci
    
                                        PACKAGE NAME   DESCRIPTION
            ________________________________________   __________________________________________________
                               gem:closest-fibonacci : version: (0.1.2)
                                                       Author: Kevin J. Dickerson
                                                       Homepage: http://github.com/kevindickerson
                                                       /closest-fibonacci
                           gem:closest-fibonacci-gem : version: (1.1.0)
                                                       Author: Ramprasad Ramachandran
                                                       Homepage: http://github.com/beckram23/closest-
                                                       fibonacci-gem
                               gem:closest_fibonacci : version: (1.2.13)
                                                       Author: Boris Polania
                                                       Homepage:
                                                       http://github.com/bpolania/closest_fibonacci
                                       gem:fibonacci : version: (0.1.6)
                                                       Author: Chaitanya Vellanki
                                                       Rubyforge: http://rubyforge.org/projects/fibonacci
                                                       Homepage: http://github.com/chaitanyav/fibonacci
                                   gem:fibonacci-evs : version: (0.1.2)
                                                       Author: Edward Simpson
                                                       Homepage: http://github.com/edsimpson/fibonacci-
                                                       evs
                                gem:simple_fibonacci : version: (0.1.2)
                                                       Author: Anjali Shenoy
                                                       Homepage:
                                                       http://github.com/anjshenoy/simple_fibonacci

    $ aero info gem:fibonacci

                                                       INFORMATION: fibonacci
            ________________________________________   __________________________________________________
                                             authors : Chaitanya Vellanki
                                              bindir : bin
                                                date : 2011-12-17
                                         description : A Ruby gem for exploring Fibonacci series
                                               email : me@chaitanyavellanki.com
                                            homepage : http://github.com/chaitanyav/fibonacci
                                                name : fibonacci
                                            platform : ruby
                                       require_paths : lib
                               required_ruby_version : >= 0
                           required_rubygems_version : >= 0
                                   rubyforge_project : fibonacci
                                    rubygems_version : 1.8.23
                               specification_version : 3
                                             summary : Fibonacci
                                             version : 0.1.6

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
    $ aero search npm:'fibonacci async'
    
                                        PACKAGE NAME   DESCRIPTION
            ________________________________________   __________________________________________________
                                 npm:fibonacci-async : Author: Gottox 2012-05-26
                                                       So, you want to benchmark node.js with fibonacci
                                                       once again? - Here's the library for that. You're
                                                       welcome.
                                                       Tags: 11:25

    $ aero info npm:fibonacci-async
        
                                                       INFORMATION: fibonacci-async
            ________________________________________   __________________________________________________
                                              author : Enno Boland <eb@s01.de>
                                         description : So, you want to benchmark node.js with fibonacci
                                                       once again? - Here"s the library for that. You"re
                                                       welcome.
                                                dist : tarball: http://registry.npmjs.org/fibonacci-async
                                                       /-/fibonacci-async-0.0.2.tgz
                                                       shasum: 173d4d28b038723f41bacc660edc331b1e526047
                                           dist-tags : latest: 0.0.2
                                             engines : node: *
                                                main : lib/binding.js
                                         maintainers : Gottox <g@s01.de>
                                                name : fibonacci-async
                                          repository : url: git://github.com/Gottox/fibonacci-async.git
                                          repository : type: git
                                             scripts : preinstall: node-waf clean || (exit 0); node-waf
                                                       configure build
                                                time : 0.0.1: 2012-05-26T11:24:06.960Z
                                                time : 0.0.2: 2012-05-26T11:25:45.254Z
                                             version : 0.0.2
                                            versions : 0.0.1, 0.0.2

```

Special notes:

Info uses the ``npm view`` command which return a JavaScript object of the registry which we then nudge closer to resembling JSON format so that we may proceed to parce it with **:mod:json**
                                                                                         

Pip
---
Supported commands:

* search
* install

```
    $ aero search pip:fibonacci
    
                                        PACKAGE NAME   DESCRIPTION
            ________________________________________   __________________________________________________
                                        pip:anot_fib : A simple program to return nth fibonacci number
                                       pip:fibonacci : a function of fibonacci number
                                        pip:multifib : Multiple Fibonacci Number Implementations, in
                                                       Python and C
                                        pip:myfib.py : A simple printer of fibonacci series
                                        pip:myfibbha : A simple printer of fibonacci series

```

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
            ________________________________________   __________________________________________________
                                             Version : @13.0 (irc)
                                         Description : Handy tools for being obnoxious on IRC. Warning:
                                                       some of the cows are potentially offensive.
                                            Homepage : http://gruntle.org/projects/irssi/insub/
                                           Platforms : darwin
                                             License : unknown
                                         Maintainers : nomaintainer@macports.org

```

Going forward
-------------

As well as extending the current functionality we also plan to support:

* fink
* apt-get
* composer local
* PEAR
* pip

Known issues
------------

Besides the installation being broken the following items also need attention:

* Cache uses the package key only this is not suitaby redundant but instead o a quickfix a proper cache dataset design is required to also satisfy the next item;
* Autocomplete should complete known packages obtained through searching.
* No unit tests as yet
* Limited to no codedocs

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
        
