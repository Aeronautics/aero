BREW=$(which brew)

if [ "$BREW" ]; then
    export adapter_registered=1
else
    export adapter_registered=0
fi

function brew_search {
    echo 'Searching in Homebrew'
    $BREW search $1|awk '{print $1}'
}
