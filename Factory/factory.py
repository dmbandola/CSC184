import abc
import urllib2
from BeautifulSoup import BeautifulStoneSoup

class connector(object):
    """Abstract class to connect to remote resource."""
    __metaclass__ = abc.ABCMeta #Declares class as abstract class

    def __init__(self, is_secure):
        self.is_secure = is_secure
        self.port = self.port_factory_method()
        self.protocol = self.protocol_factory_method()

    @abc.abstractmethod
    def parse(self):
        """Parses web content.
        This methis should be redefined in the runtime."""
        pass

    def read(self, host, path):
        """A generic method for all subclasses, reads web content."""
        url = self.protocol + '://' + host + ':' + str(self.port) + path
        print 'Connecting to ', url
        return urllib2.urlopen(url, timeout=2).read()

    @abc.abstractmethod
    def protocol_factory_method(self):
        """A factory method that must be redefined in subclass."""
        pass

    @abc.abstractmethod
    def port_factory_method(self):
        """Another factory method that must be redefined in subclass."""
        return FTPPort()
