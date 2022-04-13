const express = require('express');
const app = express();

app.listen(8080, function(){
    console.log('listening on 8080')
});

// 누군가가 /pet으로 방문하면..pet관련된 안내문을 띄워주자
// npm install -g nodemon 서버를 꼭 끄지 않아도 바뀌면 자동으로 반영해주는 라이브러리 
// nodemon server.js 활성화

app.get('/pet', function( 요청 , 응답){
    응답.send('펫용품 쇼핑을 할 수 있는 페이지 입니다.');
});

app.get('/beauty', function( 요청 , 응답){
    응답.send('뷰티용품 쇼핑을 할 수 있는 페이지 입니다.');
});

app.get('/', function( 요청 , 응답){
    응답.sendFile(__dirname + '/index.html');
});

app.get('/write', function( 요청 , 응답){
    응답.sendFile(__dirname + '/write.html');
});



