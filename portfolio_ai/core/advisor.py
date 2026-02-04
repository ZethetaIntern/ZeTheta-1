class RoboAdvisor:
    @staticmethod
    def recommendation(goal_return, portfolio_return, risk_category):
        if portfolio_return >= goal_return:
            return "Goal achievable with current risk profile."

        if risk_category == "Conservative":
            return "Increase investment horizon or contributions."

        if risk_category == "Moderate":
            return "Slightly increase risk exposure."

        return "Consider higher risk assets to meet goal."
