// primitives.v
// Holds pre-designed primitives

primitive udff(q, clock, data);

   output q; reg q;
   input  clock, data;

   table
      // obtain output on rising edge of clock
      // clock data q q+
      (01) 0 : ? : 0 ;
      (01) 1 : ? : 1 ;
      (0?) 1 : 1 : 1 ;
      (0?) 0 : 0 : 0 ;
      // ignore negative edge of clock
      F ? : ? : - ;
      // ignore data changes on steady clock
      ? (??) : ? : - ;
   endtable

endprimitive // u_dff


`timescale 1ns / 1ps
`celldefine
module dff(clock, q, data);
   input clock, data;
   output q;

   udff(q, clock, data);

   specify
      // arc clk --> q
      (posedge clock => ( q +: data )) = (0.1, 0.1);
   endspecify

endmodule // udff
`endcelldefine
