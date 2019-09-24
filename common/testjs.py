import execjs

code1 = """

             <html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312"/>
<title>js  form 表单传递变量参数</title>
</head>
<body>
<form id="testForm"  name="testForm" method="post" >
<input type="text" name="name" />

<input type="button" onClick="to_submit();" value="提交"/>
</form>
<script language="javascript">
   //定义变量
   var str='hello';
   //获取form表单     
   var formdeal= document.getElementById("testForm");
   //制定表单action地址，可以加一些变量参数
   formdeal.action="deal.php?parms="+str;
   alert( formdeal.action);
   //制定跳转页面打开方式，默认的是_self,如果想在新窗口打开，可以用_blank
   formdeal.target="_self";

   //提交表单
   formdeal.submit();

}
</script>
</body>
</html>
        """

#execjs.eval(code1)
