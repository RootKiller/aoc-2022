const std = @import("std");
const io = std.io;
const fs = std.fs;

pub fn calculatePriority(item: u32) u32 {
    if ((item >= 'a') and (item <= 'z')) {
        return 26 - ('z' - item);
    }
    if ((item >= 'A') and (item <= 'Z')) {
        return 52 - ('Z' - item);
    }
    return 0;
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();
    defer {
        _ = gpa.deinit();
    }

    const stdout = std.io.getStdOut().writer();

    const cwd = fs.cwd();
    const file = try cwd.openFile("input.txt", .{ .mode = .read_only });
    defer file.close();

    var file_reader = file.reader();

    var duplicatedProprities = std.ArrayList(u32).init(allocator);
    defer duplicatedProprities.deinit();
    var total : u32 = 0;

    var buffer: [500]u8 = undefined;
    while (try file_reader.readUntilDelimiterOrEof(buffer[0..], '\n')) |line| {
        if (line.len % 2 != 0) {
            try stdout.print("Line {s} has odd character count, wrong data\n", .{line});
            return error.Failure;
        }

        var half = line.len / 2;
        var first_compartment = line[0..half];
        var second_compartment = line[half..line.len];

        for (first_compartment) |first_item| {
            var first_item_priority = calculatePriority(first_item);
            
            for (second_compartment) |second_item| {
                var second_item_priority = calculatePriority(second_item);

                if (first_item_priority == second_item_priority) {
                    if (std.mem.indexOfScalar(u32, duplicatedProprities.items, first_item_priority) == null) {
                        total += first_item_priority;
                        try duplicatedProprities.append(first_item_priority);
                    }
                }
            }
        }

        duplicatedProprities.clearRetainingCapacity();
    }

    try stdout.print("Output {any}\n", .{total});
}

