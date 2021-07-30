/*
获取天气
load_weather：从接口获取天气
*/

function load_weather()
{
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function()
	{
		if (xmlhttp.readyState==4 && xmlhttp.status==200)
		{
            var str = xmlhttp.responseText;
            var json_str = JSON.parse(str);
            var day = json_str["data"]["total_day"];
            var city = "长安";
            var xmlhttp2 =  new XMLHttpRequest();
            xmlhttp2.onreadystatechange = function()
            {
                if (xmlhttp2.readyState==4 && xmlhttp2.status==200)
                {
                    var str = xmlhttp2.responseText;
                    var json_str = JSON.parse(str);
                    var temperature = Number(json_str["data"]["temperature"]);
                    var rain_num = Number(json_str["data"]["rain_num"]);
                    var weather = json_str["data"]["weather"];
                    var season = json_str["data"]["season"];
                    var day = json_str["data"]["day"];
                    document.getElementById("temperature").innerHTML = temperature.toFixed(2);
                    document.getElementById("rain").innerHTML = rain_num.toFixed(2);
                    document.getElementById("weather").innerHTML = weather;
                    document.getElementById("season").innerHTML = " 今天是" + season + "的第";
                    document.getElementById("day").innerHTML = day + "天";
                    if (weather == "晴")
                    {
                        document.getElementById("weather-svg").innerHTML = "<img src=\"civitas/svg/weather/qingtian.svg\"/>";
                    }
                    else if (weather == "多云")
                    {
                        document.getElementById("weather-svg").innerHTML = "<img src=\"civitas/svg/weather/duoyun.svg\"/>";
                    }
                    else if (weather == "阴")
                    {
                        document.getElementById("weather-svg").innerHTML = "<img src=\"civitas/svg/weather/yintian.svg\"/>";
                    }
                    else if (weather == "小雨")
                    {
                        document.getElementById("weather-svg").innerHTML = "<img src=\"civitas/svg/weather/xiaoyu.svg\"/>";
                    }
                    else if (weather == "大雨")
                    {
                        document.getElementById("weather-svg").innerHTML = "<img src=\"civitas/svg/weather/dayu.svg\"/>";
                    }
                    else if (weather == "小雪")
                    {
                        document.getElementById("weather-svg").innerHTML = "<img src=\"civitas/svg/weather/xiaoxue.svg\"/>";
                    }
                    else if (weather == "大雪")
                    {
                        document.getElementById("weather-svg").innerHTML = "<img src=\"civitas/svg/weather/daxue.svg\"/>";
                    }
                    else if (weather == "台风")
                    {
                        document.getElementById("weather-svg").innerHTML = "<img src=\"civitas/svg/weather/taifeng.svg\"/>";
                    }
                }
            }
            xmlhttp2.open("GET","https://api.trickydeath.xyz/getweather/?city=" + city + "&day=" + day,true);
            xmlhttp2.send();
		}
	}
    xmlhttp.open("GET","https://api.trickydeath.xyz/getdate/",true);
    xmlhttp.send();
}