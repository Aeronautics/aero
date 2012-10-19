# -*- coding: utf-8 -*-
__author__ = 'nickl-'

class CacheProvider():
    data = {}
    def seen(self, key, val=False):
        try:
            for k, v in key.items():
                self.data[k] = v
            return
        except AttributeError:
            pass

        if val:
            self.data[key] = val

        try:
            return self.data[key]
        except KeyError:
            return False

    def invalidate(self, key, expires=None):
        if isinstance(expires, bool):
            del self.data[key]
        elif isinstance(key, bool):
            self.data = {}
        elif expires == None:
            return False # check if key is valid

class BeakerCacheProvider():
    cache = None
    def seen(self, key, val=False):
        try:
            for k, v in key.items():
                self.cache.put(k, v)
            return
        except AttributeError:
            pass

        if val or not isinstance(val,bool):
            self.cache.put(key, val)

        try:
            return self.cache.get(key)
        except KeyError:
            return False

    def invalidate(self, key, expires=None):
        if isinstance(expires, bool):
            self.cache.remove_value(key)
        elif isinstance(key, bool):
            self.cache.clear()
        elif expires == None:
            return False # check if key is valid

class CacheProviderFactory():
    def whichProvider (self):
        try: import beaker
        except: pass

        if (beaker):
            from beaker.cache import CacheManager
            from beaker.util import parse_cache_config_options

            cache_opts = {
                'cache.type': 'file',
                'cache.data_dir': '/tmp/cache/data',
                'cache.lock_dir': '/tmp/cache/lock'
            }

            cache = CacheManager(**parse_cache_config_options(cache_opts))
            BeakerCacheProvider.cache =  cache.get_cache('aero.cache', type='file', expire=604800)

            return BeakerCacheProvider()
        else:
            return CacheProvider()
