import checkin


if __name__ == "__main__":
    params = '_userDate=&appVersionName=3.46.104&gameId=20001&roleName=%25E8%258D%2592%25E9%2587%258E%25E7%259A%2584%25E7%2581%25B5%25E9%25AD%2582%25CE%25BA&uniqueRoleId=2164133858&nickname=%25E5%25B7%259B%25E5%25B7%259B%25E5%25B7%259B%25E5%25BD%25A1&token=NWwus8E7&userId=97013499&serverName=%25E6%2589%258BQ222%25E5%258C%25BA&roleId=1195099075&appOpenid=27B4E004417B52674AE0A1F147615317&appVersion=2019346104&areaId=1&role=%25E8%258D%2592%25E9%2587%258E%25E7%259A%2584%25E7%2581%25B5%25E9%25AD%2582%25CE%25BA&platid=1&gameOpenid=FDE570AA47C6548B41270A642B25B777&wi=0&uin=27B4E004417B52674AE0A1F147615317&z=1232&zn=%25E5%25AE%2589%25E5%258D%2593%25E6%2589%258BQ222%25E5%258C%25BA&toOpenid=FDE570AA47C6548B41270A642B25B777&serverId=1232&roleJob=%25E6%25B0%25B8%25E6%2581%2592%25E9%2592%25BB%25E7%259F%25B3III&isMainRole=1&areaName=%25E5%25AE%2589%25E5%258D%2593&roleLevel=30&qi=1&algorithm=v2&appid=1105200115&encode=2&openid=27B4E004417B52674AE0A1F147615317&sig=da6b5ae78093a09d67b5d37be81fa0c2&source=smoba_zhushou&timestamp=1595736774498&version=3.1.96a&msdkEncodeParam=60AA522896B77F8E9361CC57FB234B6EE20C01E928591A618E98DD9A18F980ACE9A05E184F174854F22799269E90CE5C359F723FA4BAD4162F32C55D3E2F9742E324397878ADEFFEA26AD884DD2F6407EE2491E42D00D9F691A4CC85308381EE1B51F1ACCCE50C9631BD0A4BCFFF5101ADE465B12D099AED433EF57B10205DE4D5B23F26741157990838F0CA91FEDA3F008B418C25DC2E0E6BB293FA322F08CBD19501B3DA7B7E3158442D7E0B40DA17&gameOpenId=FDE570AA47C6548B41270A642B25B777&time=&cSystem=android&msdkToken=7e8AW9nn&h5Get=1'

    checkin.checkin(params)