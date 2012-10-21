var sys = arbor.ParticleSystem(1000, 400,1);
function plot() {
	sys.parameters({gravity:false});
	sys.renderer = Renderer("#viewport") ;
	var data = {
	   nodes:{
		 animals:{'color':'red','shape':'rect','label':'Animals'},
		 dog:{'color':'green','shape':'rect','label':'dog'},
		 cat:{'color':'blue','shape':'rect','label':'cat'}
	   }, 
	   edges:{
		 animals:{ dog:{}, cat:{} }
	   }
	 };
	sys.graft(data);

	// добавляем еще раз
	var postLoadData = {
	   nodes:{
		 joe:{'color':'orange','shape':'rect','label':'joe'},
		 fido:{'color':'green','shape':'rect','label':'fido'},
		 fluffy:{'color':'blue','shape':'rect','label':'fluffy'}
	   }, 
	   edges:{
			dog:{ fido:{} },
			cat:{ fluffy:{} },
			joe:{ fluffy:{},fido:{} }
	   }
	 };
	sys.graft(postLoadData);
}