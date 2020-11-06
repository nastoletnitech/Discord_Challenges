imie = gets.chomp
if !(3..13).include? imie.length
    puts 'imie nie jest poprawne'
    exit!
end
if !imie[-1].eql? 'a' or imie.downcase.eql? 'kuba'
    puts 'imie jest meskie'
else
    puts 'imie jest zenskie'
end
