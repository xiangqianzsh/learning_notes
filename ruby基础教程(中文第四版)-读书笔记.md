
# ruby基础教程（中文第四版)-读书笔记

## 第 21 章　Proc 类
### 练习题1
```ruby
def my_collect(obj, &block)
  if block
    obj.each_with_index do |item, idx |
      obj[idx] = block.call(item)
    end
  end
end

ary = my_collect([1, 2, 3, 4, 5]) do |i|
  i * 2
end

p ary  #=> [2, 4, 6, 8, 10]
```

### 练习题2
```ruby
to_class = :class.to_proc
p to_class.call("test")    #=> String
p to_class.call(123)       #=> Fixnum
p to_class.call(2 ** 1000) #=> Bignum
```

### 练习题3
```ruby
def accumlator
  total = 0
  Proc.new do |i|
    total += i
  end
end

acc = accumlator
p acc.call(1)    #=> 1
p acc.call(2)    #=> 3
p acc.call(3)    #=> 6
p acc.call(4)    #=> 10
```