#ruby 相关知识

@(ruby笔记)

理解 Ruby Symbol (Ruby中的冒号)
http://blog.csdn.net/besfanfei/article/details/7966850


a =|| b
if != nil
    return a
else
    return b

ruby OptionParser
http://ruby-doc.org/stdlib-1.9.3/libdoc/optparse/rdoc/OptionParser.html


__FILE__这个变量代表文件自己的文件名，在foo.rb中puts__FILE__，结果就是foo.rb。
ruby中__FILE__与$0之间的区别

http://blog.sina.com.cn/s/blog_622439560101i2aq.html

puts __FILE__  #当前文件名-->绝对路径 --> 所在目录名
puts File.expand_path(__FILE__)  #当前文件名-->绝对路径 
puts File.dirname(File.expand_path(__FILE__))  #当前文件名-->绝对路径 --> 所在目录名

shift unshift
ruby 数组

 http://blog.sina.com.cn/s/blog_6a55d9950100v4xu.html


 
 Ruby中puts、p和print的区别? 
http://blog.chinaunix.net/uid-21843387-id-3294617.html

ruby 中默认赋值的变量可以是函数的输入变量，于Python 不同
def f(x, y=x)
  print x, y
end
f(3)
#结果33


abort
abort(message) ((<ruby 1.7 特性>))
以非正常方式结束Ruby程序的运行。它与Exit的区别在于，调用时若$!不为nil的话，就将异常消息输出到标准错误输出当中；另外，程序的结束status始终都是EXIT_FAILURE(在绝大多数环境中都是1)。

ruby 1.7 特性:若指定了message参数的话，就将message赋值给SystemExit#message后输出到标准错误输出中。


GENERIC_OPTIONS = %w[D fs jt files libjars archives]
print GENERIC_OPTIONS  # ["D", "fs", "jt", "files", "libjars", "archives"]
[Ruby]转载: 关于ruby中 %Q, %q, %W, %w, %x, %r, %s 的用法
http://www.cnblogs.com/buhaiqing/p/3537558.html



ruby元编程 那些书里没有的知识 define_method
http://www.cnblogs.com/IAmBetter/archive/2013/03/16/2963696.html



Python's equivalent for Ruby's define_method?
http://stackoverflow.com/questions/5449244/pythons-equivalent-for-rubys-define-method
Programmatically adding methods to classes and objects: more Ruby/Python comparisons
http://positiveincline.com/index.php/2009/06/programmatically-adding-methods-to-classes-and-objects-more-rubypython-comparisons/

#ruby, define_method
def do_somthing(name, age)
  print "I'am #{name}, I'am #{age} years old\n"
end
[:Lilei, :John].each do |n|
  define_method n do |age|
    do_somthing(n, age)
  end
end

Lilei(3)  # I'am Lilei, I'am 3 years old
John(4)  # I'am John, I'am 4 years old


ruby 中如何得到当前运行的类的名字和函数的名字， 在logger记录, 找bug
class A
  def f(x)
    puts self.class
    puts __method__
  end

  def g(x)
    print x
  end
end

a = A.new
a.f(3)
puts "#{a.class}"




def f(x, y)
  args =  method(__method__).parameters.map { |arg| arg[1].to_s}
  print args.map { |arg| "#{arg} = #{eval arg}" }.join(', ')
end
f(3, 4)
Is there a way to access method arguments in Ruby?
http://stackoverflow.com/questions/9211813/is-there-a-way-to-access-method-arguments-in-ruby




#http://ruby-doc.org/core-2.2.3/Kernel.html#method-i-set_trace_func
```ruby
p = proc do |event, filename, lineno, object_id, binding, class_name|
  if event == 'call'
    puts "#{event}, #{filename}, #{lineno}, #{object_id}, #{class_name}"
    binding.local_variables.each do |var|
      puts "#{var}: #{binding.local_variable_get(var)}"
    end
  end
end
```
set_trace_func(p)  #所有以下的部分都会监听
```
class A
  @b = 2
  def f(x)
    y=4
    print x
  end

end

A.new.f(3)
```

#更好的办法
#http://ruby-doc.org/core-2.2.3/Kernel.html#method-i-set_trace_func
```ruby
p = proc do |event, filename, lineno, object_id, binding, class_name|
  if event == 'call'
    puts "#{event}, #{filename}, #{lineno}, #{object_id}, #{class_name}"
    binding.local_variables.each do |var|
      next unless class_name.new.method(object_id).parameters.any? { |_, param| param == var }
      puts "#{var}: #{binding.local_variable_get(var)}"
    end
  end
end

```
set_trace_func(p)  #所有以下的部分都会监听
```
class A
  @b = 2
  def f(x)
    y=4
    print x
  end

end
A.new.f(3)



def g(x)
  print x
end

g(3)
```
更更好：
```ruby
p = proc do |event, filename, lineno, object_id, binding, class_name|
    if event == 'call'
        puts "#{event}, #{filename}, #{lineno}, #{object_id}, #{class_name}"
        binding.local_variables.each do |var|
            next unless class_name.instance_method(object_id).parameters.any? { |_, param| param == var }
            puts "#{var}: #{binding.local_variable_get(var)}"
        end
    end
end
```

```ruby
p = proc do |event, filename, lineno, object_id, binding, class_name|
  filename_s = filename.split("/")[-1]
  #   if event == 'call' and ["framework.rb", "streaming.rb", "run.rb"].include?(filename_s)
    if event == 'call'  and filename.include?("E:")
        s = "E:/learn prog/logstat/logstat2"
        filename_s = filename.gsub!(/#{"E:/learn prog/logstat/logstat2"}/,'.')
#
        class_name = (class_name.class == Class or class_name.class == Module) ? class_name : class_name.class
        puts "#{filename_s} -> #{class_name} -> #{object_id}() -> #{lineno}"
#
        binding.local_variables.each do |var|
            next unless class_name.instance_method(object_id).parameters.any? { |_, param| param == var }
            puts "#{' '*10}#{var}: #{binding.local_variable_get(var)}"
        end
    end
end
set_trace_func(p)
```

还有个问题，最好用STDERR.puts
不然可能影响正常输出


windowns 
gem install oj-2.12.12.gem --local





在字典中{a: 3} 相当于 {:a => 3}

