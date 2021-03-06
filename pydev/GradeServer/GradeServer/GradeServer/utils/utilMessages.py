# -*- coding: utf-8 -*-

from flask import render_template, session
from datetime import datetime

"""
나쁜 말 & 좋은 말 메세지 모음
"""
def get_message(key ='unknown'):
    messageDict = {'unknown': '죄송 합니다. 알수 없는 에러 입니다.',
                  'login': 'Login!!!',
                  'tryAgain': '다시 시도해 주시기 바랍니다.',
                  'accessFailed': '접근 할 수 있는 권한이 없습니다.',
                  'invalidAccess': 'don\'t access through URL',
                  'updateSucceeded': 'Update Succeeded!!!!',
                  'updateFailed': '정보 갱신에 실패하였습니다.',
                  
                  'pattenFailed': '암호에 아이디나 현재 암호를 입력 할 수 없습니다.',
                  'notExists': '해당 아이디가 없습니다.',
                  'alreadyExists': '이미 있는 아이디 입니다.',
                  'wrongPassword': '암호가 일치하지 않습니다.',
                  'fillData': '를(을) 입력해 주시기 바랍니다.',
                  
                  'writtenComment': '댓글을 작성 하였습니다!!!',
                  'deletedComment': '댓글을 삭제 하였습니다!!!',
                  'writtenPost': '게시물을 작성 하였습니다!!!',
                  'banPosting': '글을 작성 할 수 없습니다.',
                  'modifiedPost': '게시물을 수정 하였습니다!!!',
                  'modifiedComment': '댓글을 수정 하였습니다!!!',
                  'deletedPost': '게시물을 삭제 하였습니다!!!',
                  
                  'acceptInvitee': '팀에 합류 되었습니다!!!',
                  'rejectInvitee': '팀 초대를 거절 하셨습니다!!!',
                  'notSelf': '자기 자신을 설정 할 수 없습니다.',
                  'notTeamMemberInvitee': '팀 원을 초대 할 수 없습니다.',
                  'inviteeSucceeded': '님을 초대 하였습니다!!!',
                  'existTeamName': '같은 팀 명이 존재 합니다.',
                  'makeTeamSucceeded': '팀이 만들어졌습니다!!!',
                  'removeTeamSucceeded': '팀이 삭제 되었습니다!!!',
                  
                  'dbError' : "DB 에러입니다. 다시 제출해 주세요.", 
                  'serverError' : "서버 오류입니다. 다시 제출해 주세요.",
                  'fileError' : "파일 관련 오류입니다. 다시 제출해 주세요." ,
                  'askToMaster' : "관리자한테 문의하세요."}

    return messageDict[key]


"""
오류로 인한  메인  페이지 이동
"""
def unknown_error(error = None):    
    from GradeServer.utils.utilArticleQuery import select_notices
    from GradeServer.utils.utilRankQuery import select_top_coder
    
    from GradeServer.resource.htmlResources import HTMLResources
    from GradeServer.resource.sessionResources import SessionResources
    
    #from GradeServer.GradeServer_logger import Log
    
    isLogin = len(session._get_current_object())
    if isLogin:
        isLogin = session[SessionResources().const.MEMBER_ID_INDEX]
        memberIdIndex = session[SessionResources().const.MEMBER_ID_INDEX]
    else:
        memberIdIndex = None
        
    return render_template(HTMLResources().const.MAIN_HTML,
                           noticeRecords = select_notices(memberIdIndex,
                                                          isLogin),
                           topCoders = select_top_coder(),
                           error = error)
