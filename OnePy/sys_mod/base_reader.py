class DataReaderBase(object):

    """负责读取数据"""

    env = None

    def __init__(self, ticker, fromdate=None, todate=None):
        self.ticker = ticker
        self.fromdate = fromdate
        self.todate = todate
        self.env.readers[self.ticker] = self