# require 'auto_click' 
require 'tty-reader'

keyboard = TTY::Reader.new

# simon - AutoClick.new

running = true

puts "Program started..."

while(running)

    keyboard.on(:keyescape) do
        running = false
    end

end

puts "Program stopped."