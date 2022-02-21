import requests
import pytest

user_agent1 = "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
user_agent2 = "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"
user_agent3 = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
user_agent4 = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"
user_agent5 = "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"

user_agents = {
    user_agent1,
    user_agent2,
    user_agent3,
    user_agent4,
    user_agent5
}


class Test13:
    @pytest.mark.parametrize('user_agent', user_agents)
    def test_user_agent_check(self, user_agent):
        response = requests.get(
            'https://playground.learnqa.ru/ajax/api/user_agent_check',
            headers={"User-Agent": user_agent}
        )
        platform = response.json()['platform']
        browser = response.json()['browser']
        device = response.json()['device']
        if user_agent == user_agent1:
            exp_platform = 'Mobile'
            exp_browser = 'No'
            exp_device = 'Android'
        else:
            if user_agent == user_agent2:
                exp_platform = 'Mobile'
                exp_browser = 'Chrome'
                exp_device = 'iOS'
            else:
                if user_agent == user_agent3:
                    exp_platform = 'Googlebot'
                    exp_browser = 'Unknown'
                    exp_device = 'Unknown'
                else:
                    if user_agent == user_agent4:
                        exp_platform = 'Web'
                        exp_browser = 'Chrome'
                        exp_device = 'No'
                    else:
                        exp_platform = 'Mobile'
                        exp_browser = 'No'
                        exp_device = 'iPhone'
        assert platform == exp_platform, f"Platform in {user_agent} defined incorrectly"
        assert browser == exp_browser, f"Browser in {user_agent} defined incorrectly"
        assert device == exp_device, f"Device in {user_agent} defined incorrectly"
