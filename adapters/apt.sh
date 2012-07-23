if [ "$(which apt-get)" ]; then
    export adapter_registered=1
else
    export adapter_registered=0
fi

