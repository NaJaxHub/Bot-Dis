local whitelistPak = {
    {
        Hwid = "0000000000000000000",
        Key = "893294010762928149",
        Verify = true
    },
    {
        Hwid = "1-2-3-4-5",
        Key = "s",
        Verify = true
    },
    {
        Hwid = "1-2-3-4-5",
        Key = "sf",
        Verify = true
    },
    {
        Hwid = "1-2-3-4-5",
        Key = "0101",
        Verify = false
    },
    {
        Hwid = "xxx",
        Key = "yyy",
        Verify = false
    },
    {
        Hwid = "xjxx",
        Key = "yyyj",
        Verify = false
    },
}
return whitelistPak