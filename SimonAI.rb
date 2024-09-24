require 'io/console'
require 'auto_click'

simon_ai = AutoClick.new

running = true

puts "Program started..."

Thread.new {
    while(running)

        simon_ai.type("a")

    end
    char = STDIN.getch
    
    if char == "\u0003"
        exit
    end
}

puts "Program stopped."