
class MathController < ApplicationController
  def add
    result = 2 + 2
    render plain: result.to_s
  end
end
