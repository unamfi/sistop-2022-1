#!/usr/bin/ruby
# coding: utf-8

if ARGV[0].nil?
  STDERR.puts 'Ejemplo de invocación:'
  STDERR.puts $0 + ' nombre_datos "descripción del equipo"'
  STDERR.puts 'Se espera que exista un archivo nombre_datos.txt.'
  exit 1
end

basename = ARGV[0]
sysdescr = ARGV[1]

if ! File.exists?("#{basename}.txt")
  STDERR.puts "El archivo #{basename}.txt no existe"
  exit 2
end

times = {}
iter=1
max_time=0
rf = open("#{basename}.txt","r")
plot=open("#{basename}.gnuplot", 'w')
data = open("#{basename}.data","w")

rf.readlines.each do |lin|
  next unless lin =~ /^(real|user|sys)\s+(\d+)m([\d\.]+)s/
  which = $1
  min = $2.to_f
  sec = $3.to_f
  time = min*60 + sec
  max_time = time if time > max_time

  times[iter] ||= {}
  times[iter][which] = time

  iter+=1 if which=='sys'
end

plot.puts <<"EOF"
reset
set term pngcairo fontscale 2 size 2048,1536
set output '#{basename}.png'
data="#{basename}.data"

set grid
set title 'Tiempo requerido para la compilación del núcleo de Linux • #{sysdescr}'
set xlabel 'Número de núcleos utilizado'
set xrange [0.8:#{iter}]
set ylabel 'Tiempo requerido para la compilación (s / mm:ss)'
set yrange [0:#{((max_time / 1000).to_i + 1) * 1000}]
set key left top

EOF

times.keys.sort.each do |t|
  data.puts('%d %f %f %f' % [t, times[t]['real'], times[t]['user'], times[t]['sys']] )
  plot.puts 'set label "%d:%02d" rotate by 30 at first %d, first %f' %
            [(times[t]['real']/60).to_i, times[t]['real'] % 60, t, times[t]['real']]
  plot.puts 'set label "%d:%02d" rotate by 330 at first %d, first %f' %
            [(times[t]['user']/60).to_i, times[t]['user'] % 60, t, times[t]['user']]
  plot.puts 'set label "%d:%02d" rotate by 45 at first %d, first %f' %
            [(times[t]['sys']/60).to_i, times[t]['sys'] % 60, t, times[t]['sys']]
end

plot.puts <<EOF

plot data using 1:2 with linespoints linetype rgb "#30cc70" lw 4 title "Tiempo efectivo", \
          data using 1:3 with linespoints linetype rgb "#cc3070" lw 1 title "Tiempo de usuario (secuencial)", \
     data using 1:4 with linespoints linetype rgb "#3070cc" lw 1 title "Tiempo sistema (secuencial)"
EOF

plot.close
data.close

system('gnuplot', "#{basename}.gnuplot")

