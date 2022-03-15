def head(f):
    f.write('''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8",name="viewport" content="width=device-width, initial-scale=1" >
    <meta http-equiv="refresh" content="30">
    <title>justgo</title>
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC&display=swap');
        @import url('https://fonts.googleapis.com/earlyaccess/cwtexfangsong.css');
        @import url('https://fonts.googleapis.com/earlyaccess/cwtexyen.css');
        @media (min-width: 600px) {
        p {
            font-size: 20px;
          }
        }
        </style>
</head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script type="text/javascript">
    $(document).ready(function(){
    $(".flip").click(function(){
        $(".panel").slideToggle("slow");
      });
    });
    $(document).ready(function(){
    $(".flip2").click(function(){
        $(".panel2").slideToggle("slow");
      });
    });
    $(document).ready(function(){
    $(".flip3").click(function(){
        $(".panel3").slideToggle("slow");
      });
    });
</script>
<style type="text/css"> 
    div.panel,p.flip
    {
    margin:0px;
    padding:5px;
    text-align:center;
    background:#005AB5;
    border:solid 1px #E0E0E0;
    }
    div.panel
    {
    height:100%;
    display:none;
    }

    div.panel2,p.flip2
    {
    margin:0px;
    padding:5px;
    text-align:center;
    background:#005AB5;
    border:solid 1px #E0E0E0;
    }
    div.panel2
    {
    height:100%;
    display:none;
    }
    div.panel3,p.flip3
    {
    margin:0px;
    padding:5px;
    text-align:center;
    background:#005AB5;
    border:solid 1px #E0E0E0;
    }
    div.panel3
    {
    height:100%;
    display:none;
    }
</style>
<style type="text/css">
body {
margin-top: 0px;
margin-right: 0px;
margin-bottom: 0px;
margin-left: 0px;
}
#container{
height:100%;
margin-top:0px;
background: -webkit-linear-gradient(#005AB5,#005757);
background: -o-linear-gradient(#005AB5,#005757);
background: -moz-linear-gradient(#005AB5,#005757);
background: linear-gradient(#005AB5,#005757);
}
</style>
<style>
ul.pagination {
    display: inline-block;
    padding: 0;
    margin: 0;
}

ul.pagination li {display: inline;}

ul.pagination li a {
    color: black;
    float: left;
    padding: 8px 16px;
    text-decoration: none;
}
</style>
<body>
    <center>
    <div id="container">
    <div style="background-color:#9CC2E6;">
    <img src="justgopic.png" width="300" height="150">
    <br>
    <span style="font-family:cwTeXYen";><span style="font-size:50px;"><font color="#000000"><u>歡迎使用揪車</span><span style="font-family:Comic Sans MS;"><span style="font-size:50px;">just go</font></u></h1></span>
    </div>
''')
