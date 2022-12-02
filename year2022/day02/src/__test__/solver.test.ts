import { expect } from "chai";
import "mocha";

import { readExample, readInput } from "../lib";
import { readData } from "../reader";
import { solveA, solveB } from "../solver";

describe("Day02Solver", () => {
  describe("Part A", () => {
    it("returns the example solution", () => {
      const input = readData(readExample());
      const result = solveA(input);

      expect(result).to.be.equal(15);
    });

    it("returns the solution", () => {
      const input = readData(readInput());
      const result = solveA(input);
      expect(result).to.be.equal(14297);
    });
  });

  describe("Part B", () => {
    it("returns the example solution", () => {
      const input = readData(readExample());
      const result = solveB(input);

      expect(result).to.be.equal(12);
    });

    it("returns the solution", () => {
      const input = readData(readInput());
      const result = solveB(input);
      expect(result).to.be.equal(10498);
    });
  });
});
