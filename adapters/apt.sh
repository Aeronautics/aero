APT=$(which apt-get)
APT_CACHE=$(which apt-cache)

if [ "$APT" ]; then
    export adapter_registered=1
else
    export adapter_registered=0
fi

function apt_search {
    echo "Searching in APT"
    $APT_CACHE search $1|awk '{print $1}'
}
