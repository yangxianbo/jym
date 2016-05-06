(function(){
    var M = window.M = function(selector,content) { return new M.fn.init(selector,content);};
    M.fn = M.prototype = { 
	//event:event||window.event,
	init: function(selector) { 
	   selector = selector || document;
	 if(selector=="body"){
	  this[0]=document.getElementsByTagName("body")[0];
	  return this;
	 }
     if(selector.nodeType){
	   //alert(11)
	   this[0] = selector;
	   this.node=selector;
       this.length = 1;
       return this;
	 }
     if (typeof selector == "string"){
	   if(selector.indexOf('#') == 0){
	        var id = selector.substring(1);
		    this[0] = document.getElementById(id);
	        this.length = 1;
	        this.node=selector;
	   }else{
	        this[0]=document.getElementsByTagName(selector)[0];
	   }
	  
	   return this;
	 }
	  if(selector) this.selector = selector;
	  return this; 
	},
    create:function(tagname){
	   //alert(this[0])
	    this.tag=document.createElement(tagname);
		if(this[0]){
		  this[0].appendChild(this.tag)
		}
		
		this[0]=this.tag;
		//this.style(defaultStyle);
	    return this;
	},
	remove:function(selector){
	    if(!this[0])return;
		if(!this[0].parentNode)return;
	    this[0].parentNode.removeChild(this[0]);
        return this;
	},
	draw:function(ele){
	   obj=this[0];
	   
	   var oldx=0,oldy=0,oldobj=null;
	   obj.onmousedown=function(event){
	      
	      var event=event||window.event;	
          oldobj=this;
          var EX=event.x||event.pageX;
          var EY=event.y||event.pageY;
          oldx=EX-oldobj.offsetLeft;oldy=EY-oldobj.offsetTop;
		  
	   }
	   obj.onmousemove=function(event){
	           var event=event||window.event;	
               var EX=event.x||event.pageX;
               var EY=event.y||event.pageY;
               if(oldobj==null){return false}
                    oldobj.style.left=(EX-oldx)+"px";;
                    oldobj.style.top=(EY-oldy)+"px";
	    }
		obj.onmouseup=function(event){
		   if(oldobj!=null){oldobj=null}
		}
	},
	css:function(cla){
	   this[0].className=cla;
	   return this
	},
	style:function(param,ele){
	    
	    if(!param){return this}
		var stylejson=param;
	    var obj=!ele?this[0]:ele;
		for (var x in stylejson){
		  obj.style[x]=stylejson[x];
		}
		//alert(this[0])
		return this;
	},
	pro:function(param,ele){
	    if(!param){return this}
		var obj=!ele?this[0]:ele;
		for (var x in param){
		  obj.setAttribute(x,param[x]);
		  //console.log(obj[firstChild]);
		}
		return this;
	},
	move:function(param,ele){
	   if(!param){return this}
	   var obj=!ele?this[0]:ele;
	  // this.offset=0;
	   var that=this;
	   this.timeid=setInterval(function(){
	      var offset=0;
	      if (param.way=="right"){
	         offset+=param.offset;
	      }
		  if (param.way=="left"){
	         offset-=param.offset;
	      }
		  //alert(obj.offsetLeft)
		  //alert(param.offset+"---"+that.offset+"--"+(param.offset+that.offset))
		 // alert(obj.offsetLeft)
		 
	     obj.style.left=obj.offsetLeft+offset+"px";
		 //alert(obj.offsetRight)
	   },param.sec)
	   return this;
	},
	html:function(value,ele){
	    if(!value){return this}
		obj=!ele?this[0]:ele;
		if(!obj)return this
		obj.innerHTML=value;
		return this
	},
	
	nInput:function(){
	   if(!this[0])return;
	   this[0].oninput=function(e){
	    this.value=this.value.replace(/[^\d]/g,'')
	   }
	},
	/*
	**{
	  *content:[]下拉组合框内容数组
	  *Mstyle:{}容器样式
	  *Cstyle:{}内容样式
	}
	*/
    combobox:function(param){
	    if(!param)return;
		var d;//下拉DIV
		var liArr=[];//内容li数组
	    var obj=this[0];
		var X;
		var Y;
		var H;
		var main={
		  Mstyle:function(){
		    d.style(param.Mstyle);
		  },
		  Cstyle:function(){
            //alert(liArr.length)
		    for(i=0;i<liArr.length;i++){
			  
			  M(liArr[i]).style(param.Cstyle);
			}
		  },
		  //定位
		  pos:function(){
		    
		    X=M.pageX(obj);
			Y=M.pageY(obj);
			H=obj.offsetHeight;
		    style={
		    left:X+"px",
		    top:Y+H+"px",
		    height:"auto",
		    width:obj.offsetWidth-2+"px",
		    background:"#fff",
		    border:"1px solid #000",
		    position:"absolute", 
			
			
		    }
		  },
		  create:function(){
		    main.pos();
		    if(M("#m_combobox")[0]){
			  d=M("#m_combobox")
			}else{
				d=M("body").create("div").style(style).pro({id:"m_combobox"});
			}
		    
			d[0].innerHTML="";
			//alert(11);
		    var arr=param.content;
		    var u=M(d[0]).create("ul").style({margin:0,padding:0})
			if(arr.length<=0){
				var li=M(u[0]).create("li").html("无查询结果").style(listyle);
			}
		    for (i=0;i<arr.length;i++){
		       var li=M(u[0]).create("li").html(arr[i]['val']).style(listyle).pro({value:arr[i]["key"]});
			   liArr[i]=li[0];
		       li[0].onmouseup=function(){
		         obj.value=this.value;
		         main.over();
				 if(param.click){
					 param.click(this.value,this.innerHTML);
				 }
		       }
			   li[0].onmouseover=function(){
			     M(this).style(listOver)
			   }
			   li[0].onmouseout=function(){
			     M(this).style(listOut)
			   }
		    }
			
			M("body")[0].onmouseup=function(e){
			        
				      if(e.target!=obj){
					     main.over();
					  }
		    }
			
			if(param.Mstyle){main.Mstyle(param.Mstyle);}
			if(param.Cstyle){main.Cstyle(param.Cstyle);}
		  },
		  over:function(){
		     M("body")[0].onclick=null;
		     M("#m_combobox").remove();
			 d=false;
			 //alert(d)
		  }
		}
		//下拉框DIV样式
		
		var style={}
		//下拉框列表样式
		var listyle={listStyleType:'none',cursor:"pointer"}
		var listOver={background:"#D7EBF9",}
		var listOut={background:"none"}
		//$(obj).bind("input",function(){main.over()});
		main.create();
		$(obj).bind("click",function(){main.create()})
			
		//obj.onclick=function(){if(!d)main.create();}
	
	}
	}
    M.fn.init.prototype = M.fn
	M.select=function(elem){alert(this.pageX)}
	M.GetscrollTop=function(){return document.documentElement.scrollTop || document.body.scrollTop;}
	M.GetscrollLeft=function(){return document.documentElement.scrollLeft || document.body.scrollLeft;}
	M.scrollTop=function(pos,speed){
	   var X=50;//频率内位移像素
       var speed=10//定时器频率
       var scrT=M.GetscrollTop();//滚动之前滚动条X位置
       var Tox=pos;//要滚动到的X位置
       var Tway=scrT-Tox<0?true:false;//ture表示向下滑动,false表示向上滑动.
       var Toy=obj.offsetLeft;
       var timeid= window.setInterval(function(){
       if(Tway){
	      if(M.GetscrollTop>=Tox){window.scrollTo(0,Tox);window.clearInterval(timeid)}
		  else{window.scrollTo(0,M.GetscrollTop()+X);}
	   }else{
	      if(M.GetscrollTop()<=Tox){window.scrollTo(0,Tox);window.clearInterval(timeid)}
		  else{window.scrollTo(0,M.GetscrollTop()-X);}
	   }
	 
     
	
  },speed);
	}
	//取元素相对整个文档X位置
	M.pageX=function(elem){
	   var p = 0;
       while(elem.offsetParent ){
        p += elem.offsetLeft;
        elem = elem.offsetParent;
       }
       return p;
	}
    M.get=function(key){
	    var search=location.search.substr(1);
		var arr=search.split("&");
		var i=0;
		var GET={};
		for(i=0;i<arr.length;i++){
		    var kvarr=arr[i].split("=");
			 
			if(!kvarr[1]){
			
			  kvarr[1]="";
			}
			GET[kvarr[0]]=kvarr[1];
		}
		return GET[key];
	}
	/*window.onload=function(){
	    M.loadcss('window.css');
	    M.window({})
	}*/
	//加载CSS
	M.loadcss=function(name){
	   var path=M.loadpath()+name;
	   var pro={
	     rel:"stylesheet",
		 type:"text/css",
		 href:path,
	   }
	  var s= M('head').create("link").pro(pro);
	  console.log(s[0]);
	}
	//取主题css加载路径
	M.loadpath=function(){  
	  var link=$("link");
	  var i;
	  for(i=0;i<link.length;i++){
	    if(link[i].href.toString().search(/m.css/)!=-1){  
		   var path=link[i].href;
		}	
	  }
	  path=path.replace(/m.css/,"");
	  return path;
	}
	//取元素相对整个文档Y位置
	M.pageY=function(elem){
	   var p = 0;
       while ( elem.offsetParent ) {
        p += elem.offsetTop;
        elem = elem.offsetParent;
       }
       return p;
	}
    M.window=function(param){
	
	   if(!param){return}
	   var mainDiv=M("body").create("div").css('window');
	   M(mainDiv[0]).draw();
	   /*var defaultstyle={
		 position:"fixed",
		 border:"1px solid #689ADD",
	   }
	   var titlestyle={
	     lineHeight:"25px",
         color:"#0E2D5F",
         fontSize:"14px",
         fontWeight:"600",
		 position:"absolute",
		 top:"-25px",
		 height:"25px",
		 background:"#EEF3FA",
		 width:"100%",
	   }
	   var mainDiv=M("body").create("div").style(defaultstyle).style(param.style);
	   var navDiv=M(mainDiv[0]).create("div").style(titlestyle);
	   var titleSpan=M(navDiv[0]).create("span").html("new window").style({marginLeft:"20px"});
	    //alert(mainDiv.tag)*/
	}

	$.fn.extend({
	     create:function(ele){
		    var re=M(this[0]).create(ele);
			return re;
		 },
	   	 banner:function(param){
		 var param=param?param:{};
         $.easing.def="easeOutBounce";//设置默认效果
		 var ele=$(this[0]);//主DIV
		 var allul=$(ele).find("ul");//所有UL
         var ul=$(allul[0]);//导航UL
		 var li=$(ul[0]).find("li");//导航LI
		 var allli=allul.find("li");
		 var mdiv=M(ele[0]).create('div');//创建翻页DIV
		 var mul=mdiv.create("ul");//创建翻页UL
		 var tempDiv=$(mdiv[0]);
		 var tempUl=$(mul[0]);
		 var tempLi='';
		 var ispage=false;
		 var liNum=li.length;//li数量
		 var i;
	     for(i=0;i<liNum;i++){//创建翻页LI
			 var lx=M(tempUl[0]).create('li').pro({value:i});
			 $(lx[0]).click(function(){showPage(this.value)});
	     }
		 tempLi=tempUl.find("li");
		 var liWidth;//每个LI长度
		 var pageNow=0;//当前页数
		  //初始化数据
		 var init=function(){
		     var width=ele.width(); 
			 liWidth=width;//获取li宽度
			 var elestyle={overflow:"hidden"};
		     var style={Width:width};
			 var allulstyle={margin:0,padding:0};
			 var alllistyle={listStyleType:"none"};
			 var tempDivstyle={width:width,position:"absolute"}
			 var tempUlstyle={padding:0,marginTop:"-20px",textAlign:"center"};
			
			 var tempLIdefaultstyle={
			   display:"inline-block",
			 }
			 var tempListyle={height:"10px",width:"10px",
			  background:"#f5f5f5",border:"1px solid #e9e9e9",
			  marginLeft:"10px",
			 }
			
			 var ulstyle={
			   width:width*liNum,
			   height:"100%",
			   position:"relative",
			 };
			 var listyle={
			  width:width,
			  height:"100%",
			  cssFloat:"left",
			  styleFloat:"left",
			 }
		     ele.css(style);
			 ele.css(elestyle);
			 allli.css(alllistyle);
			 allul.css(allulstyle);
			 ul.css(ulstyle);
			 li.css(listyle);
			 tempDiv.css(tempDivstyle);
			 tempUl.css(tempUlstyle);
			 tempLi.css(tempLIdefaultstyle);
			 
			 if(param.pagelicss){
			   tempLi.addClass(param.pagelicss);
			 }else{
			   tempLi.css(tempListyle);
			 }
		 }
        
		 //定义内部函数开始
		 //显示指定页数
		 var showPage=function(index,animate){
			if(index==pageNow)return;
		    if(ispage==true)return;
		    var ulLeft=0-(index*liWidth);
			if(!animate){
			    ispage=true;
			   if(index==0){
			     ul.css('left',0-(liWidth));
			     ul.animate({left:0},{duration:800,
                complete: callback});
			  }else{
			    ul.animate({left:ulLeft},{duration:800,
                complete: callback});
			  }
			  
			}else{
			    ul.css('left',ulLeft);
				return;
			}
			
			lightTemp(index);
		    pageNow=index;
		 }
		 //高亮index页LI
		 var lightTemp=function(index){
		      var tempLi=$(tempUl[0]).find('li');
			  var i;
			  for(i=0;i<tempLi.length;i++){
			     if(tempLi[i]==tempLi[index]){
				    //当前页样式
				    $(tempLi[i]).css('background','#5EBADF');
					$(tempLi[i]).css('border','1px dotted #5EBADF');
				 }else{
				    //原样式
				    $(tempLi[i]).css('background','#e9e9e9');
					$(tempLi[i]).css('border','1px solid #666');
				 }
			  }
		 }
		
		  //动画完成后回调函数
         var callback=function (){
		    ispage=false;
		    showPage(pageNow,true);
			if(param.callback){
			  param.callback(pageNow);
			}
         } 
		 //开始自动轮播并返回定时器ID
		 var auto=function(){
		    var timeID=setInterval(function(){ 
				  if(pageNow+1>=liNum){
				  //自动轮播到最后一页后下一页变为第一页
				    pageNow=-1;
				  }
				  showPage(pageNow+1);
		    },3000);
			return timeID;
		 }
		 //定义内部函数结束
		 $(window).resize(function(){
		   init();
		   if(pageNow!=0){showPage(pageNow,true)}
		 });
		 init();
		 $(function(){
		    init();
			lightTemp(0);
		 })
		
		 var timeid=auto();
		 ele.mouseover(function(){
		    if(timeid!=0){
			  clearInterval(timeid);
			  timeid=0;
			}
		 })
		 ele.mouseout(function(){
		   if(timeid==0){
		      timeid=auto();
			 // alert(timeid);
		   }
		 })
	   },
	   cBox:function(param){
	      M(this[0]).combobox(param)
	   },
	   Data:function(ele){
	      //if(!ele)return;
		  var obj=$(this[0]).find("[name]");
		  var i;//循环变量
		  //alert(obj[2].value)
		  var data={};//json对象
		  for(i=0;i<obj.length;i++){ 
		     var type=obj[i].type;
			 switch (type){
			   case "checkbox":
			   data[obj[i].name]=[];
			   break;
			   case "radio":
			   if(obj[i].checked==true){
			   data[obj[i].name]=obj[i].value
			
			   }
			   
			   break;
			   default:
			   data[obj[i].name]=obj[i].value;
			 }
				
		  }
		  var checked=$(this[0]).find("input:checked");
		  if(checked.length>0){
		    
		    for(i=0;i<checked.length;i++){
			   var name=checked[i].name;
               data[name][i]=checked[i].value;
			}
		  }
		  return data;
	   }
	})
	String.prototype.trim = function()  
   {  
   return this.replace(/(^\s*)|(\s*$)/g, "");  
   }  
	
})();