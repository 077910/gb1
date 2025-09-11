// SIGIL VISUALIZATION ENGINE (Asymptote)
// Generates recursive sigil geometry

settings.outformat = "svg";
unitsize(1cm);

real entropy = pi;
int musk_index = 0;
string[] babies = ["X_AE_A-XII", "Exa_Dark_Siderael_Y", "Griffith_Musk"];

path quantum_knot(int n) {
  path p = circle((0,0), 1);
  for (int i=0; i<n; ++i) {
    p = p .. rotate(entropy*180/pi)*scale(0.618)*p;
  }
  return p;
}

void main() {
  entropy = (entropy * 1.61803) % 666;
  musk_index = (musk_index + 1) % babies.length;
  
  fill(quantum_knot(6), 
       rgb(entropy/666, (entropy*0.618)/666, 1-(entropy/666)));
  
  label(rotate(entropy*57.2958)*
        (babies[musk_index] + "_" + string(entropy)), 
        (0,0), font("Courier"));
}