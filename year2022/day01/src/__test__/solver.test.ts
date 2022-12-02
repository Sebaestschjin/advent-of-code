import { expect } from "chai";
import "mocha";

import { readExample, readInput } from "../lib";
import { readData } from "../reader";
import { solveA, solveB } from "../solver";

describe("Day01", () => {
  describe("Part A", () => {
    it("returns the example solution", () => {
      const input = readData(readExample());
      const result = solveA(input);

      expect(result).to.be.equal(24000);
    });

    it("returns the solution", () => {
      const input = readData(readInput());
      const result = solveA(input);

      expect(result).to.be.equal(69836);
    });
  });

  describe("Part B", () => {
    it("returns the example solution", () => {
      const input = readData(readExample());
      const result = solveB(input);

      expect(result).to.be.equal(45000);
    });

    it("returns the solution", () => {
      const input = readData(readInput());
      const result = solveB(input);

      expect(result).to.be.equal(207968);
    });
  });
});
