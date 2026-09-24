# TradeRelax Invest - Open-Source Technical Analysis & Research Tool
# Bu skript maliýe bazarlaryndaky tehnik görkezijileri we barlaglary simulasiýa etmek üçin ýazyldandyr.

class TechnicalAnalysisTool:
    def __init__(self, asset_name):
        self.asset_name = asset_name
        self.history = []

    def calculate_rsi(self, prices, period=14):
        """
        RSI (Relative Strength Index) barlag we hasaplama funksiýasy.
        """
        if len(prices) < period:
            return "Maglumat ýetmezçilik edýär."
        
        gains = []
        losses = []
        
        for i in range(1, len(prices)):
            change = prices[i] - prices[i-1]
            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))
                
        avg_gain = sum(gains[-period:]) / period
        avg_loss = sum(losses[-period:]) / period
        
        if avg_loss == 0:
            return 100.0
            
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return round(rsi, 2)

    def log_analysis(self, result):
        self.history.append(result)
        print(f"[{self.asset_name}] Analiz netijesi ýatda saklanyldy: {result}")

# Mmysal ulanylyşy:
if __name__ == "__main__":
    tool = TechnicalAnalysisTool("EUR/USD OTC")
    sample_prices = [1.0850, 1.0855, 1.0852, 1.0860, 1.0858, 1.0865]
    rsi_result = tool.calculate_rsi(sample_prices)
    tool.log_analysis(f"RSI Barlagy: {rsi_result}")
