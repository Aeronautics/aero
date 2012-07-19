if [ "$(which apt-get)" ]; then
    export provider_registered=1
else
    export provider_registered=0
fi
