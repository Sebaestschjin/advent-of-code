import { readFileSync } from "fs";

export const readExample = () => {
  return readFileSync(__dirname + "/../res/example.in", { encoding: "utf-8" });
};

export const readInput = () => {
  return readFileSync(__dirname + "/../res/in", { encoding: "utf-8" });
};

export const lines = (input: string): string[] => {
  return input.split("\n").filter((l) => l.trim().length > 0);
};

export const sum = (values: number[]): number => {
  return values.reduce((p, v) => p + v, 0);
};
