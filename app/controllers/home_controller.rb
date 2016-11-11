# coding: utf-8
class HomeController < ApplicationController
  def top
    @ad = 1

    #検索フォームに入力があれば、その条件でタスクを取得
    #if params[:title].present?
    #  @page = Page.all
    #  @page = @page.where(@page.arel_table[:title].matches("%#{params[:title]}%"))
    #end

    @page = Page.order("number").reverse_order.page(params[:page]).per(40)
  end

  def about
    @ad = 1
  end

  def inqury
  end
  
  def video
  end

end
