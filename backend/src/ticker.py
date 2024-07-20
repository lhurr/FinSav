import yfinance as yf
from cachetools import TTLCache
import logging
import quantstats as qs
from cachetools.func import ttl_cache
import plotly.graph_objects as go


show = False

class _TickerData:
    _ticker_info_cache = TTLCache(maxsize=1024, ttl=60)
    FAST_INFO = ['currency', 'dayHigh', 'dayLow', 'exchange', 'fiftyDayAverage', 'lastPrice', 'lastVolume', 'marketCap', 'open', 'previousClose', 'quoteType', 'regularMarketPreviousClose', 'shares', 'tenDayAverageVolume', 'threeMonthAverageVolume', 'timezone', 'twoHundredDayAverage', 'yearChange', 'yearHigh', 'yearLow']

    @staticmethod
    @ttl_cache(ttl=3600, maxsize=1024)
    def download_returns(symbol):
        returns = qs.utils.download_returns(symbol)
        return returns

    @staticmethod
    def get_data(symbol, method_name):
        if symbol not in _TickerData._ticker_info_cache:
            logging.info(f"Create ticker {symbol}")
            _TickerData._ticker_info_cache[symbol] = yf.Ticker(symbol)

        values = getattr(_TickerData._ticker_info_cache[symbol], method_name)
        return values

    @staticmethod
    def get_fast_info(symbol):
        info = _TickerData.get_data(symbol, "info")
        fast_info = {
            key: info.get(key, "") for key in _TickerData.FAST_INFO
        }
        return fast_info


class TickerInfo:

    @staticmethod
    def company_info(**kwargs):
        info = _TickerData.get_data(kwargs.get("symbol"), "info")
        officers = info.get("companyOfficers", [])
        fast_info = _TickerData.get_fast_info(kwargs.get("symbol"))
        fast_info.update({
            "symbol": info.get("symbol", ""),
            "exchange": info.get("exchange", ""),
            "address": info.get("address1", ""),
            "city": info.get("city", ""),
            "state": info.get("state", ""),
            "zip": info.get("zip", ""),
            "country": info.get("country", ""),
            "phone": info.get("phone", ""),
            "website": info.get("website", ""),
            "industry": info.get("industry", ""),
            "sector": info.get("sector", ""),
            "longBusinessSummary": info.get("longBusinessSummary", ""),
            "longName": info.get("longName", ""),
            "shortName": info.get("shortName", ""),
            "fullTimeEmployees": info.get("fullTimeEmployees", ""),
        })
        return fast_info, None

    @staticmethod
    def valuation_measures(**kwargs):
        info = _TickerData.get_data(kwargs.get("symbol"), "info")
        return {
            "symbol": info.get("symbol", ""),
            "marketCap": info.get("marketCap", 0),
            "enterpriseValue": info.get("enterpriseValue", 0),
            "currency": info.get("currency", ""),
            "beta": info.get("beta", 0),
            "trailingPE": info.get("trailingPE", 0),
            "forwardPE": info.get("forwardPE", 0),
            "pegRatio": info.get("pegRatio", 0),
            "priceToSalesTrailing12Months": info.get("priceToSalesTrailing12Months", 0),
            "priceToBook": info.get("priceToBook", 0),
            "enterpriseToRevenue": info.get("enterpriseToRevenue", 0),
            "enterpriseToEbitda": info.get("enterpriseToEbitda", 0)
        }, None

    @staticmethod
    def trading_information(**kwargs):
        info = _TickerData.get_data(kwargs.get("symbol"), "info")
        return {
            "symbol": kwargs.get("symbol"),
            "priceHint": info.get("priceHint", 0),
            "previousClose": info.get("previousClose", 0),
            "open": info.get("open", 0),
            "dayLow": info.get("dayLow", 0),
            "dayHigh": info.get("dayHigh", 0),
            "regularMarketPreviousClose": info.get("regularMarketPreviousClose", 0),
            "regularMarketOpen": info.get("regularMarketOpen", 0),
            "regularMarketDayLow": info.get("regularMarketDayLow", 0),
            "regularMarketDayHigh": info.get("regularMarketDayHigh", 0),
            "currency": info.get("currency", ""),
            "financialCurrency": info.get("financialCurrency", ""),
            "currentPrice": info.get("currentPrice", 0),
            "volume": info.get("volume", 0),
            "regularMarketVolume": info.get("regularMarketVolume", 0),
            "beta": info.get("beta", 0),
            "trailingPE": info.get("trailingPE", 0),
            "forwardPE": info.get("forwardPE", 0),
            "priceToBook": info.get("priceToBook", 0),
            "pegRatio": info.get("pegRatio", 0),
            "trailingPegRatio": info.get("trailingPegRatio", 0),
            "bid": info.get("bid", 0),
            "ask": info.get("ask", 0),
            "bidSize": info.get("bidSize", 0),
            "askSize": info.get("askSize", 0),
            "marketCap": info.get("marketCap", 0),
            "targetHighPrice": info.get("targetHighPrice", 0),
            "targetLowPrice": info.get("targetLowPrice", 0),
            "targetMeanPrice": info.get("targetMeanPrice", 0),
            "targetMedianPrice": info.get("targetMedianPrice", 0),
            "recommendationMean": info.get("recommendationMean", 0),
            "recommendationKey": info.get("recommendationKey", ""),
        }, None

    @staticmethod
    def dividend_data(**kwargs):
        info = _TickerData.get_data(kwargs.get("symbol"), "info")
        return {
            "symbol": kwargs.get("symbol"),
            "dividendRate": info.get("dividendRate", 0),
            "dividendYield": info.get("dividendYield", 0),
            "payoutRatio": info.get("payoutRatio", 0),
            "fiveYearAvgDividendYield": info.get("fiveYearAvgDividendYield", 0),
            "trailingAnnualDividendRate": info.get("trailingAnnualDividendRate", 0),
            "trailingAnnualDividendYield": info.get("trailingAnnualDividendYield", 0),
            "lastDividendValue": info.get("lastDividendValue", 0),
        }, None

    @staticmethod
    def financial_summary(**kwargs):
        info = _TickerData.get_data(kwargs.get("symbol"), "info")
        return {
            "symbol": kwargs.get("symbol"),
            "totalCash": info.get("totalCash", 0),
            "totalCashPerShare": info.get("totalCashPerShare", 0),
            "ebitda": info.get("ebitda", 0),
            "totalDebt": info.get("totalDebt", 0),
            "quickRatio": info.get("quickRatio", 0),
            "currentRatio": info.get("currentRatio", 0),
            "totalRevenue": info.get("totalRevenue", 0),
            "debtToEquity": info.get("debtToEquity", 0),
            "revenuePerShare": info.get("revenuePerShare", 0),
            "returnOnAssets": info.get("returnOnAssets", 0),
            "returnOnEquity": info.get("returnOnEquity", 0),
            "freeCashflow": info.get("freeCashflow", 0),
            "operatingCashflow": info.get("operatingCashflow", 0),
            "earningsQuarterlyGrowth": info.get("earningsQuarterlyGrowth", 0),
            "netIncomeToCommon": info.get("netIncomeToCommon", 0),
            "trailingEps": info.get("trailingEps", 0),
            "forwardEps": info.get("forwardEps", 0),
            "earningsGrowth": info.get("earningsGrowth", 0),
            "revenueGrowth": info.get("revenueGrowth", 0),
            "grossMargins": info.get("grossMargins", 0),
            "ebitdaMargins": info.get("ebitdaMargins", 0),
            "operatingMargins": info.get("operatingMargins", 0),
            "financialCurrency": info.get("financialCurrency", "")
        }, None

    @staticmethod
    def show_stock_performance(**kwargs):
        returns = _TickerData.download_returns(kwargs.get("symbol"))
        fig = qs.plots.snapshot(returns, show=show, )
        fig.title = f'{kwargs.get("symbol")} Performance'
        return {
            "symbol": kwargs.get("symbol"),
            "data": _TickerData.get_fast_info(kwargs.get("symbol")),
        }, fig

    @staticmethod
    def show_stock_cumulative_returns(**kwargs):
        returns = _TickerData.download_returns(kwargs.get("symbol"))
        fig = qs.plots.returns(returns, show=show, benchmark=None)
        fig.title = f'{kwargs.get("symbol")} Cumulative Returns'
        return {
            "symbol": kwargs.get("symbol"),
            "data": _TickerData.get_fast_info(kwargs.get("symbol")),
        }, fig

    @staticmethod
    def show_stock_log_returns(**kwargs):
        returns = _TickerData.download_returns(kwargs.get("symbol"))
        fig = qs.plots.log_returns(returns, show=show, benchmark=None)
        fig.title = f'{kwargs.get("symbol")} Log Cumulative Returns'
        return {
            "symbol": kwargs.get("symbol"),
            "data": _TickerData.get_fast_info(kwargs.get("symbol")),
        }, fig

    @staticmethod
    def show_stock_daily_returns(**kwargs):
        returns = _TickerData.download_returns(kwargs.get("symbol"))
        fig = qs.plots.daily_returns(returns, show=show, benchmark=None)
        fig.title = f'{kwargs.get("symbol")} Daily Returns'
        return {
            "symbol": kwargs.get("symbol"),
            "data": _TickerData.get_fast_info(kwargs.get("symbol")),
        }, fig

    @staticmethod
    def show_stock_yearly_returns(**kwargs):
        returns = _TickerData.download_returns(kwargs.get("symbol"))
        fig = qs.plots.yearly_returns(returns, show=show, benchmark=None)
        fig.title = f'{kwargs.get("symbol")} EOY Returns'
        return {
            "symbol": kwargs.get("symbol"),
            "data": _TickerData.get_fast_info(kwargs.get("symbol")),
        }, fig

    @staticmethod
    def show_stock_rolling_beta(**kwargs):
        returns = _TickerData.download_returns(kwargs.get("symbol"))
        fig = qs.plots.rolling_beta(returns, show=show, benchmark='SPY')
        fig.title = f'{kwargs.get("symbol")} Rolling Beta To SPY'
        return {
            "symbol": kwargs.get("symbol"),
            "data": _TickerData.get_fast_info(kwargs.get("symbol")),
        }, fig

    @staticmethod
    def show_stock_rolling_sharpe(**kwargs):
        returns = _TickerData.download_returns(kwargs.get("symbol"))
        fig = qs.plots.rolling_sharpe(returns, show=show)
        fig.title = f'{kwargs.get("symbol")} Rolling Sharpe (6-Months)'
        return {
            "symbol": kwargs.get("symbol"),
            "data": _TickerData.get_fast_info(kwargs.get("symbol")),
        }, fig

    @staticmethod
    def show_stock_rolling_sortino(**kwargs):
        returns = _TickerData.download_returns(kwargs.get("symbol"))
        fig = qs.plots.rolling_sortino(returns, show=show)
        fig.title = f'{kwargs.get("symbol")} Rolling Sortino (6-Months)'
        return {
            "symbol": kwargs.get("symbol"),
            "data": _TickerData.get_fast_info(kwargs.get("symbol")),
        }, fig

    @staticmethod
    def show_stock_rolling_volatility(**kwargs):
        returns = _TickerData.download_returns(kwargs.get("symbol"))
        fig = qs.plots.rolling_volatility(returns, show=show)
        fig.title = f'{kwargs.get("symbol")} Rolling Volatility (6-Months)'
        return {
            "symbol": kwargs.get("symbol"),
            "data": _TickerData.get_fast_info(kwargs.get("symbol")),
        }, fig

    @staticmethod
    def show_stock_monthly_return_heatmap(**kwargs):
        returns = _TickerData.download_returns(kwargs.get("symbol"))
        fig = qs.plots.monthly_heatmap(returns, show=show)
        fig.title = f'{kwargs.get("symbol")} Monthly Returns (%)'
        return {
            "symbol": kwargs.get("symbol"),
            "data": _TickerData.get_fast_info(kwargs.get("symbol")),
        }, fig

    @staticmethod
    def show_ohlc_price_volume_history(**kwargs):
        symbol = kwargs.get("symbol")
        data = _TickerData.get_data(symbol, "history")(period='2y').reset_index()
        fig = go.Figure(
            data=go.Ohlc(
                x=data['Date'],
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])
        )
        title = f'{kwargs.get("symbol")} latest Open-High-Low-Close Chart'
        fig.update_layout(
            title=title,
        )
        return {
            "symbol": kwargs.get("symbol"),
            "data": f"{data.iloc[0].__str__()}\n-----\n{data.iloc[-1].__str__()}\n-----\nInfo: {_TickerData.get_fast_info(symbol)}",
        }, fig

