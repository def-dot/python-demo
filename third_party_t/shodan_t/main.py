import shodan


class ShodanT:
    def __init__(self):
        self.api = shodan.Shodan("")

    def search_cursor(self):
        self.api.search_cursor()

    def search_t(self):
        try:
            # Search Shodan
            results = self.api.search('apache')
            # Show the results
            print('Results found: {}'.format(results['total']))
            for result in results['matches']:
                print('IP: {}'.format(result['ip_str']))
                print(result['data'])
                print('')
        except shodan.APIError as e:
            print('Error: {}'.format(e))

    def facet_t(self):
        try:
            # Search Shodan
            facets = [
                "org",
                "domain",
                "port",
                "asn",
                ("country", 3)
            ]
            results = self.api.count('apache', facets=facets)
            for facet in results['facets']:
                print(f"facet {facet}")
                for t in results['facets'][facet]:
                    print(f"value {t['value']} count {t['count']}")
                print("")
        except shodan.APIError as e:
            print('Error: {}'.format(e))

    def host_t(self):
        try:
            host = self.api.host('103.224.182.253')
            # Print general info
            print("""
                    IP: {}
                    Organization: {}
                    Operating System: {}
            """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

            # Print all banners
            for item in host['data']:
                print("""
                            Port: {}
                            Banner: {}

                    """.format(item['port'], item['data']))
        except shodan.APIError as e:
            print('Error: {}'.format(e))


if __name__ == "__main__":
    t = ShodanT()
    t.search_t()
    # t.host_t()
    # t.facet_t()
