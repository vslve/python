import unittest

import regions_source as rs

response = rs.get_response_body()
fact_total = response['total']
fact_default_page = response['items']


class TestTotal(unittest.TestCase):
    def test_total(self):
        self.assertEqual(rs.get_total(), fact_total)


class TestPageSize(unittest.TestCase):
    def test_default_page_size(self):
        self.assertEqual(rs.default_page_size, len(fact_default_page))

    def test_correct_page_sizes(self):
        for page_size in rs.correct_page_sizes:
            self.assertEqual(len(rs.get_by_params(rs.params['by_page_size'], page_size)), page_size)

    def test_incorrect_page_size(self):
        for page_size in rs.incorrect_page_sizes:
            self.assertTrue(
                'error' in rs.get_by_params(rs.params['by_page_size'], page_size, correct=False),
                msg=f'correct for page size {page_size}'
            )


class TestCountryCode(unittest.TestCase):
    def test_correct_country_codes(self):
        for country_code in rs.correct_country_codes:
            codes = rs.get_country_codes(rs.get_by_params(rs.params['by_country_code'], country_code))
            self.assertEqual(len(codes), 1, msg=f'codes for country code {country_code}: {codes}')
            self.assertTrue(country_code in codes, msg=f'different country code: {codes} instead {country_code}')

    def test_incorrect_country_code(self):
        for country_code in rs.incorrect_country_codes:
            regions = rs.get_by_params(rs.params['by_country_code'], country_code, correct=False)
            self.assertTrue('error' in regions, msg=f'correct for country code {country_code}')

    def test_default_country_code(self):
        allowed_codes = set(rs.correct_country_codes)
        listed_codes = rs.get_country_codes(rs.get_regions())
        self.assertTrue(len(listed_codes) >= len(allowed_codes), msg=f'not all country listed by default')


class TestPageNumber(unittest.TestCase):
    def test_default_page(self):
        default_page = rs.get_by_params(
            rs.params['by_page'], rs.default_page_number,
            rs.params['by_page_size'], len(fact_default_page)
        )
        self.assertEqual(default_page, fact_default_page, msg=f'page default value is not {rs.default_page_number}')

    def test_last_page(self):
        total = rs.get_total()

        for page_size in rs.correct_page_sizes:
            last_page_number = rs.get_page_count(page_size, total)
            last_page_size = rs.get_last_page_size(page_size, total)
            fact_last_page_size = len(rs.get_by_params(
                rs.params['by_page'], last_page_number,
                rs.params['by_page_size'], page_size
            ))
            after_last_page_size = len(rs.get_by_params(
                rs.params['by_page'], last_page_number + 1,
                rs.params['by_page_size'], page_size
            ))

            self.assertEqual(
                fact_last_page_size,
                last_page_size,
                msg=f'for page size {page_size} last page contains {fact_last_page_size} instead {last_page_size}'
            )
            self.assertEqual(after_last_page_size, 0, msg=f'pages after last content page is not empty')

    def test_min_page_number(self):
        previous_page = rs.get_by_params(rs.params['by_page'], rs.min_page_number - 1)
        self.assertTrue('error' in previous_page, msg=f'min page number is not equal {rs.min_page_number}')


class TestRegionNameSearch(unittest.TestCase):

    def test_search_by_correct_substring(self):
        for substring in rs.correct_names_substring:
            sb = rs.get_encoded_ascii(substring)
            regions = map(lambda x: x['name'].lower(), rs.get_by_params(rs.params['by_substring'], sb))
            for region in regions:
                self.assertTrue(substring.lower() in region, msg=f'for substring: {substring} region name: {region}')

    def test_search_by_incorrect_substring(self):
        for substring in rs.incorrect_names_substring:
            sb = rs.get_encoded_ascii(substring)
            self.assertTrue(
                'error' in rs.get_by_params(rs.params['by_substring'], sb, correct=False),
                msg=f'correct for substring: {substring}'
            )

    def test_multi_params(self):
        default_params = [
            rs.params['by_substring'],
            rs.get_encoded_ascii(rs.params_default_values['by_substring']),
        ]
        params = [
            (param_type, value) for (param_type, value) in
            zip(rs.params.values(), rs.params_default_values.values()) if param_type != default_params[0]
        ]

        result = rs.get_by_params(*default_params)

        for param in params:
            if param[0] == rs.params['by_substring']:
                param = (param[0], rs.get_encoded_ascii(param[1]))

            self.assertEqual(
                result, rs.get_by_params(*default_params, *param),
                msg=f'different content for parameters {param}'
            )

        self.assertEqual(
            result,
            rs.get_by_params(*default_params, *[x for pair in params for x in pair]),
            msg=f'different content for parameters {params}'
        )


if __name__ == '__main__':
    unittest.main()
