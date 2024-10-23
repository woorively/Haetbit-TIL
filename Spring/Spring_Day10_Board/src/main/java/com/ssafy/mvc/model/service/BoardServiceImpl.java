package com.ssafy.mvc.model.service;

import java.util.List;

import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import com.ssafy.mvc.model.dao.BoardDao;
import com.ssafy.mvc.model.dto.Board;
import com.ssafy.mvc.model.dto.SearchCondition;


@Service
public class BoardServiceImpl implements BoardService{
	private final BoardDao boardDao;
	
	public BoardServiceImpl(BoardDao boardDao) {
		this.boardDao = boardDao;
	}

	@Override
	public List<Board> getBoardList() {
		System.out.println("모든 게시글을 가져옴");
		return boardDao.selectAll();
	}

	@Override
	public Board readBoard(int id) {
		// TODO Auto-generated method stub
		boardDao.updateViewCnt(id);
		return boardDao.selectOne(id);
	}
	
	@Override
	public void writeBoard(Board board) {
		// TODO Auto-generated method stub
		boardDao.insertBoard(board);
	}
	
	@Transactional
	@Override
	public void removeBoard(int id) {
		// TODO Auto-generated method stub
		System.out.println("게시글 삭제");
		boardDao.deleteBoard(id);
		
	}
	
	@Transactional
	@Override
	public void modifyBoard(Board board) {
		// TODO Auto-generated method stub
		System.out.println("게시글 수정");
		boardDao.updateBoard(board);
		
	}

	@Override
	public List<Board> search(SearchCondition condition) {
		// TODO Auto-generated method stub
		return boardDao.search(condition);
	}
}
