/*
2024.04.05 wnwoghd22(Jay202) All Rights Reserved.

질문게시판의 임의의 질문글 페이지에 들어간 후 개발자 도구로 실행합니다.
html에서 특정 클래스인 태그만을 골라내는 단순한 스크레이퍼입니다.
https://www.acmicpc.net/ 사이트에 트래픽을 발생시키지 않습니다.
*/

// 질문 제목 추출
const questionTitle = document.querySelector('.page-header h3').textContent.trim();

// 문제 번호 추출
const problemNumber = document.querySelector('.page-header blockquote a').getAttribute('href').split('/').pop();

// JSON 배열을 저장할 변수 생성
const comments = [];

// 모든 댓글을 선택
const commentElements = document.querySelectorAll('.col-md-12.comment');

// 각 댓글을 순회하며 정보 추출
commentElements.forEach(function(commentElement) {
    // 작성자 추출
    const author = commentElement.querySelector('.panel-title a').textContent.trim();

    // 작성 일자(timestamp) 추출
    const timestamp = parseInt(commentElement.querySelector('.real-time-update').getAttribute('data-timestamp'));

    // 내용 추출
    const content = commentElement.querySelector('.content').textContent.trim();

    // textarea가 있는 경우
    var textarea = commentElement.querySelector('textarea');
    if (textarea) {
        // 언어 종류 추출
        var language = textarea.getAttribute('data-mime');
        // 코드 추출
        var code = textarea.textContent.trim();
        // JSON 객체에 코드 정보 추가
        var codeObject = {
            "language": language,
            "code": code
        };
        // JSON 배열에 추가
        comments.push({
            "author": author,
            "timestamp": timestamp,
            "content": content,
            "code": codeObject
        });
    } else {
        // textarea가 없는 경우
        // JSON 객체에 저장
        comments.push({
            "author": author,
            "timestamp": timestamp,
            "content": content
        });
    }
});

// 최종 JSON 객체 생성
const finalObject = {
    "title": questionTitle,
    "problem_id": problemNumber,
    "comments": comments
};

// JSON 객체 출력
console.log(JSON.stringify(finalObject, null, 2));
