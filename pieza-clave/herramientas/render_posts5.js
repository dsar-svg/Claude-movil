const {chromium}=require('playwright');const fs=require('fs');
const items=JSON.parse(fs.readFileSync(process.argv[2]));const out=process.argv[3];
(async()=>{const b=await chromium.launch({args:['--allow-file-access-from-files']});
for(const it of items){const p=await b.newPage({viewport:{width:it.w,height:it.h}});
fs.writeFileSync(require('path').join(__dirname,'_p.html'),'<!doctype html><meta charset=utf-8><body>'+it.html+'</body>');
await p.goto('file://'+require('path').join(__dirname,'_p.html'));await p.evaluate(()=>document.fonts.ready);await p.waitForFunction(()=>document.body.dataset.fit==="1");await p.waitForTimeout(100);
await p.screenshot({path:`${out}/${it.name}.png`});await p.close();}
await b.close();})();
