`timescale 1ns / 1ps

module nm_testbench();

   reg CK, <YOUR_PINS_HERE>;  // Add new pins in your design
   reg [35:0] RAND;
   wire [38:0] NOM_OUT, TEST_OUT;
   wire g89,g94,g98,g102,g107,g301,g306,g310,g314,g319,g557,g558,g559,g560,g561,g562,g563,g564,g705,g639,g567,g45,g42,g39,g702,g32,g38,g46,g36,g47,g40,g37,g41,g22,g44,g23;
   wire g2584_orig,g3222_orig,g3600_orig,g4307_orig,g4321_orig,g4422_orig,g4809_orig,g5137_orig,g5468_orig,g5469_orig,g5692_orig,g6282_orig,g6284_orig,g6360_orig,g6362_orig,g6364_orig,g6366_orig,g6368_orig,g6370_orig,g6372_orig,g6374_orig,g6728_orig,g1290_orig,g4121_orig,g4108_orig,g4106_orig,g4103_orig,g1293_orig,g4099_orig,g4102_orig,g4109_orig,g4100_orig,g4112_orig,g4105_orig,g4101_orig,g4110_orig,g4104_orig,g4107_orig,g4098_orig;
   wire g2584,g3222,g3600,g4307,g4321,g4422,g4809,g5137,g5468,g5469,g5692,g6282,g6284,g6360,g6362,g6364,g6366,g6368,g6370,g6372,g6374,g6728,g1290,g4121,g4108,g4106,g4103,g1293,g4099,g4102,g4109,g4100,g4112,g4105,g4101,g4110,g4104,g4107,g4098;
   integer f, i;


   // Original circuit
   s9234 original(CK,g102,g107,g1290_orig,g1293_orig,g22,g23,g2584_orig,g301,g306,g310,g314,g319,g32,g3222_orig,g36,g3600_orig,g37,g38,g39,g40,g4098_orig,g4099_orig,g41,g4100_orig,g4101_orig,g4102_orig,g4103_orig,g4104_orig,g4105_orig,g4106_orig,g4107_orig,g4108_orig,g4109_orig,g4110_orig,g4112_orig,g4121_orig,g42,g4307_orig,g4321_orig,g44,g4422_orig,g45,g46,g47,g4809_orig,g5137_orig,g5468_orig,g5469_orig,g557,g558,g559,g560,g561,g562,g563,g564,g567,g5692_orig,g6282_orig,g6284_orig,g6360_orig,g6362_orig,g6364_orig,g6366_orig,g6368_orig,g6370_orig,g6372_orig,g6374_orig,g639,g6728_orig,g702,g705,g89,g94,g98);

   // Your circuit
   s9234_scan dft(CK, <YOUR_PINS_HERE>,g102,g107,g1290,g1293,g22,g23,g2584,g301,g306,g310,g314,g319,g32,g3222,g36,g3600,g37,g38,g39,g40,g4098,g4099,g41,g4100,g4101,g4102,g4103,g4104,g4105,g4106,g4107,g4108,g4109,g4110,g4112,g4121,g42,g4307,g4321,g44,g4422,g45,g46,g47,g4809,g5137,g5468,g5469,g557,g558,g559,g560,g561,g562,g563,g564,g567,g5692,g6282,g6284,g6360,g6362,g6364,g6366,g6368,g6370,g6372,g6374,g639,g6728,g702,g705,g89,g94,g98); // Add new pins in your design

   assign {g89,g94,g98,g102,g107,g301,g306,g310,g314,g319,g557,g558,g559,g560,g561,g562,g563,g564,g705,g639,g567,g45,g42,g39,g702,g32,g38,g46,g36,g47,g40,g37,g41,g22,g44,g23} = RAND[35:0];
   assign NOM_OUT[38:0] = {g2584_orig,g3222_orig,g3600_orig,g4307_orig,g4321_orig,g4422_orig,g4809_orig,g5137_orig,g5468_orig,g5469_orig,g5692_orig,g6282_orig,g6284_orig,g6360_orig,g6362_orig,g6364_orig,g6366_orig,g6368_orig,g6370_orig,g6372_orig,g6374_orig,g6728_orig,g1290_orig,g4121_orig,g4108_orig,g4106_orig,g4103_orig,g1293_orig,g4099_orig,g4102_orig,g4109_orig,g4100_orig,g4112_orig,g4105_orig,g4101_orig,g4110_orig,g4104_orig,g4107_orig,g4098_orig};
   assign TEST_OUT[38:0] = {g2584,g3222,g3600,g4307,g4321,g4422,g4809,g5137,g5468,g5469,g5692,g6282,g6284,g6360,g6362,g6364,g6366,g6368,g6370,g6372,g6374,g6728,g1290,g4121,g4108,g4106,g4103,g1293,g4099,g4102,g4109,g4100,g4112,g4105,g4101,g4110,g4104,g4107,g4098};


   initial begin
      f = $fopen("output.txt","w");
      CK=0;
      <YOUR_CONFIG_PINS_HERE>=0;  // Configure the pins in your design
      #20;

      for (i=0; i<100000; i=i+1) begin
         #5 CK=0;
         #5 RAND={$random,$random};
         #5 CK=1;
         $fwrite(f, "%t\t%b\t%b\t%b\t%b\n", $time, RAND, NOM_OUT^TEST_OUT, NOM_OUT, TEST_OUT);
      end

      $fclose(f);
   end


endmodule // nm_testbench
